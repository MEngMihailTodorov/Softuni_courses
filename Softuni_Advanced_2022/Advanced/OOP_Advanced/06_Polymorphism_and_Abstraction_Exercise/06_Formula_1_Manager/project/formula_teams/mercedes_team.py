from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):

    @property
    def expenses_for_one_race(self):
        return 200_000

    def __init__(self, budget: int):
        super().__init__(budget)

    @property
    def sponsors(self):
        return {
            'Oracle': {
                1: 1_000_000,
                3: 500_000,
            },
            'Honda': {
                5: 100_000,
                7: 50_000,
            }
        }
