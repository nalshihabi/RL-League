use std::cmp;

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