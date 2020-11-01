use protoc_rust_grpc;
use std::ffi::OsString;
use std::path::PathBuf;
use walkdir::WalkDir;

fn main() {
    let out_dir = "src/proto_api";
    let proto_dir = "../protos";

    let proto_files: Vec<PathBuf> = WalkDir::new(proto_dir)
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
        .collect();

    // Compile protos
    protoc_rust_grpc::Codegen::new()
        .out_dir(&out_dir)
        .include(&proto_dir)
        .inputs(proto_files)
        .rust_protobuf(true)
        .run()
        .expect("Failed oh no!");

    // Make a mod.rs in the proto_api folder
    let mod_names: Vec<OsString> = WalkDir::new(out_dir)
        .into_iter()
        .filter(|e| e.as_ref().expect("Should have file or folder").file_type().is_file())
        .map(|e| {
            e.expect("Should have file")
                .path()
                .file_stem()
                .expect("No stem found")
                .to_os_string()
        })
        .collect();
}