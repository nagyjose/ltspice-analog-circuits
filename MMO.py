import numpy as np
from pymoo.core.problem import Problem

class OPAOptimizationProblem(Problem):
    def __init__(self):
        super().__init__(n_var=4,  # Number of design variables
                            n_obj=3,  # Number of objectives
                            n_constr=1,  # Number of constraints
                            xl=np.array([1e-6, 1e-6, 1e-6, 1e-12]),  # Lower bounds
                            xu=np.array([10e-6, 10e-6, 100e-6, 10e-12]))  # Upper bounds

    def _evaluate(self, x, out, *args, **kwargs):
        # Design variables
        W1, L1, I_bias, C_comp = x.T

        # Simulate circuit (replace this with actual simulation calls)
        gain = 20 * np.log10(W1 / L1)  # Placeholder
        ugb = I_bias / C_comp  # Placeholder
        power = I_bias * 1.8  # Placeholder (assuming 1.8V supply)

        # Objectives
        f1 = -gain  # Maximize gain (minimize -gain)
        f2 = -ugb   # Maximize UGB (minimize -UGB)
        f3 = power  # Minimize power

        # Constraints (e.g., gain > 60 dB)
        g1 = 20 - gain  # gain should be > 60 dB

        out["F"] = np.column_stack([f1, f2, f3])
        out["G"] = np.column_stack([g1])

problem = OPAOptimizationProblem()

#############################################################################################

from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.optimize import minimize
from pymoo.termination import get_termination

algorithm = NSGA2(pop_size=100)

termination = get_termination("n_gen", 200)

result = minimize(problem,
                  algorithm,
                  termination,
                  seed=1,
                  verbose=True)

#############################################################################################

from pymoo.visualization.scatter import Scatter

# This works if result.F is shape (N, 2) or (N, 3)
plot = Scatter()
plot.add(result.F, facecolor="blue", edgecolor="k")
plot.show()


