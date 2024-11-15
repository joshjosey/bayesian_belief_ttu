"""
The structure learn module contains several functions to learn the structure of a given data set
"""
import pandas as pd
from pgmpy.estimators import HillClimbSearch, MmhcEstimator, ExpertInLoop
from pgmpy.models import BayesianNetwork

def learn_with_hillclimb(data,scoring_method="k2score",state_names={},fixed_edges=[],black_list=[]):
    """
    Function to learn the structure of a BBN from data using hill climb search

    Input: 
        data: a pandas dataframe containing the BBN input data
        scoring_method: the scoring method to be used by the estimator
            Options: 'k2score' (default), 'bdeuscore', 'bdsscore', 'bicscore', 'aicscore', 'bic-gscore', 'aic-gscore', or StructureScore object instance
        fixed_edges: edges that must exist in the BBN structure (optional)
        black_list: edges that are forbidden in the BBN structure (optional)
    
    Output:
        model: a bayesian network found using the hill climb estimator
    """
    #Create a pgmpy HillClimbSearch object with the data to be analyzed
    est = HillClimbSearch(data, state_names=state_names)

    #Get the learned structure using the estimate function
    learned_structure = est.estimate(scoring_method=scoring_method, fixed_edges=fixed_edges,black_list=black_list)
    

    #Create the pgmpy BayesianNetwork object using our learned structure
    model = BayesianNetwork(learned_structure.edges())

    #Return the Bayesian Belief Network
    return model



def learn_with_mmhc(data,scoring_method="k2score", significance_level=0.01):
    """
    Function to learn the structure of a BBN from data using min max hill climb search

    Input: 
        data: a pandas dataframe containing the BBN input data
        scoring_method: the scoring method to be used by the estimator
            Options: 'k2score' (default), 'bdeuscore', 'bdsscore', 'bicscore', 'aicscore', 'bic-gscore', 'aic-gscore', or StructureScore object instance
        significance_level: (0.01 default) Significance level to use for conditional independence tests
    Output:
        model: a bayesian network found using the min max hill climb estimator    
    """
    #Learn the strucutre with Mmhc
    est = MmhcEstimator(data)
    estimated_structure = est.estimate(scoring_method=scoring_method,significance_level=significance_level)

    # Create the Bayesian Network
    model = BayesianNetwork(estimated_structure.edges())

    #Return the Bayesian Belief Network
    return model
