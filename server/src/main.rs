use std::thread;

use grpc;

mod agent;
mod league_runner;

mod proto_api;

use league_runner::LeagueRunnerImpl;
use proto_api::games::Agent;
use proto_api::runner_service_grpc::LeagueRunnerServer;

fn initial_agents(num_agents: usize) -> Vec<Agent> {
    (0..num_agents)
        .map(|_| Agent::new_agent(None, None))
        .collect()
}

fn begin_server(port: u16, agents: Option<Vec<Agent>>) {
    let mut server = grpc::ServerBuilder::new_plain();
    server.http.set_port(port);
    server.add_service(LeagueRunnerServer::new_service_def(LeagueRunnerImpl::new(
        agents, 5, 60,
    )));

    let _server = server.build().expect("server");

    loop {
        thread::park();
    }
}

fn main() {
    let agents = initial_agents(5);
    begin_server(50051, Some(agents));
}
