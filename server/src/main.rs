use std::thread;

use grpc;

mod agent;
mod league_runner;

mod proto_api;

use league_runner::LeagueRunnerImpl;
use proto_api::runner_service_grpc::LeagueRunnerServer;

fn main() {
    let port = 50051;

    let mut server = grpc::ServerBuilder::new_plain();
    server.http.set_port(port);
    server.add_service(LeagueRunnerServer::new_service_def(LeagueRunnerImpl::new(5, 60)));

    let _server = server.build().expect("server");

    println!(
        "greeter server started on port {}",
        port
    );

    loop {
        thread::park();
    }
}
