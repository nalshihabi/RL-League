use std::collections::{BTreeMap, BTreeSet};

use grpc;
use grpc::{ServerHandlerContext, ServerRequestSingle, ServerResponseUnarySink};
use uuid::Uuid;

use super::proto_api::{games, runner_service, runner_service_grpc};

use games::Agent;
use runner_service::{
    AgentRequest, AgentResponse, GameRequest, GameResponse, NothingResponse, ReportRequest,
};
use runner_service_grpc::LeagueRunner;

type LeagueAgentRequest = ServerRequestSingle<AgentRequest>;
type LeagueAgentResponse = ServerResponseUnarySink<AgentResponse>;
type LeagueGameRequest = ServerRequestSingle<GameRequest>;
type LeagueGameResponse = ServerResponseUnarySink<GameResponse>;
type LeagueReportRequest = ServerRequestSingle<ReportRequest>;
type LeagueNothingResponse = ServerResponseUnarySink<NothingResponse>;

pub struct LeagueRunnerImpl {
    agents: Vec<Agent>,
    max_agents: usize,
    taken_agents: BTreeSet<Agent>,
    game_timeout: usize,
    agent_map: BTreeMap<Uuid, Agent>,
}

impl LeagueRunner for LeagueRunnerImpl {
    fn request_agents(
        &self,
        o: ServerHandlerContext,
        req: LeagueAgentRequest,
        resp: LeagueAgentResponse,
    ) -> grpc::Result<()> {
        Ok(())
    }

    fn request_games(
        &self,
        o: ServerHandlerContext,
        req: LeagueGameRequest,
        resp: LeagueGameResponse,
    ) -> grpc::Result<()> {
        Ok(())
    }

    fn report_results(
        &self,
        o: ServerHandlerContext,
        req: LeagueReportRequest,
        resp: LeagueNothingResponse,
    ) -> grpc::Result<()> {
        Ok(())
    }
}

impl LeagueRunnerImpl {
    pub fn new(
        initial_agents: Option<Vec<Agent>>,
        max_agents: usize,
        game_timeout: usize,
    ) -> LeagueRunnerImpl {
        LeagueRunnerImpl {
            agents: match initial_agents {
                Some(agents) => agents,
                None => Vec::new(),
            },
            max_agents: max_agents,
            taken_agents: BTreeSet::new(),
            game_timeout: game_timeout,
            agent_map: BTreeMap::new(),
        }
    }

    // pub fn get_unique_uuid(&mut self) -> Uuid {
    //     let new_uuid = Uuid::new_v4();
    //     new_uuid
    // }
}
