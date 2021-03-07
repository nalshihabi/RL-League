extern crate protoc_rust;

use std::ffi::OsString;
use std::fs::{create_dir, File};
use std::io::Write;
use std::path::Path;
use walkdir::WalkDir;

fn main() {
    let out_dir = "src/proto_api";
    let proto_dir = "../protos";

    let proto_files: Vec<String> = WalkDir::new(proto_dir)
        .into_iter()
        .filter_map(|e| {
            let ee = e.expect("Nothing found here");
            let extension = ee.path().extension();
            if ee.file_type().is_file() && extension.unwrap_or(&OsString::from("")).eq("proto") {
                Some(ee.into_path())
            } else {
                None
            }
        })
        .map(|s| String::from(s.to_str().unwrap()))
        .collect::<Vec<String>>();

    let out_dir_path = Path::new(out_dir);
    if !out_dir_path.exists() {
        create_dir(&out_dir_path).expect("Failure in creating proto output directory.");
    }

    // Generate proto library
    protoc_rust_grpc::Codegen::new()
        .out_dir(&out_dir)
        .include(&proto_dir)
        .inputs(proto_files)
        .rust_protobuf(true)
        .run()
        .expect("Failed oh no!");

    // Generate proto library
    // Should work but doesn't for whatever reason
    // protoc_rust::Codegen::new()
    //     .out_dir(&out_dir)
    //     .include(&proto_dir)
    //     .inputs(proto_files)
    //     .run()
    //     .expect("Failed oh no!");

    // Make a mod.rs in the proto_api folder
    let mod_names: Vec<String> = WalkDir::new(out_dir)
        .into_iter()
        .filter(|e| {
            e.as_ref()
                .expect("Should have file or folder")
                .file_type()
                .is_file()
        })
        .map(|e| {
            e.expect("Should have file")
                .path()
                .file_stem()
                .expect("No stem found")
                .to_os_string()
                .to_str()
                .unwrap()
                .split(".")
                .collect::<String>()
        })
        .filter(|s| !s.eq("mod"))
        .map(|s| format!("pub mod {};", s))
        .collect();

    let mut mod_file: File = File::create(format!("{}/mod.rs", out_dir))
        .expect("Expected to successfully create new mod.rs file.");

    let mod_list = mod_names.join("\n");
    mod_file
        .write(mod_list.as_bytes())
        .expect("Error in writing mod file");
}
