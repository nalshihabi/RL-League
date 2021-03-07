use std::cmp;
use uuid::Uuid;

use super::proto_api::games;

use games::Agent;

impl cmp::PartialOrd for Agent {
    fn partial_cmp(&self, other: &Self) -> Option<cmp::Ordering> {
        Some(self.elo.cmp(&other.elo))
    }
}

impl cmp::Ord for Agent {
    fn cmp(&self, other: &Self) -> cmp::Ordering {
        self.elo.cmp(&other.elo)
    }
}

impl cmp::Eq for Agent {}

impl Agent {
    pub fn new_agent(possible_uuid: Option<String>, initial_elo: Option<i32>) -> Self {
        let uuid: String = match possible_uuid {
            Some(string) => string,
            None => format!("{}", Uuid::new_v4()),
        };
        let elo = match initial_elo {
            Some(e) => e,
            None => 1500,
        };

        let mut agent: Agent = std::default::Default::default();
        agent.uuid = uuid;
        agent.elo = elo;
        agent
    }
}
