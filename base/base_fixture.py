#处理前置条件
def deal_fixture(self, em, case_id):
    if em.fixture is not None:
        for fixture_case_id in em.fixture.split():
            if fixture_case_id.startswith("post"):
                self.test_post(fixture_case_id)
            elif fixture_case_id.startswith("get"):
                self.test_get(fixture_case_id)
            elif fixture_case_id.startswith("fixture"):
                self.Initialize_order(fixture_case_id, case_id)





