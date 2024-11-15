from process_data import process_lung_data
from structure_learn import learn_with_hillclimb, learn_with_mmhc
from draw_bbn import draw_bbn

def main():
    #Let the user know the program began
    print("Starting TTU BBN...\n")

    #Call the process_lung_data to get a processed dataframe
    data = process_lung_data('./data/Lung_Cancer_Data.csv')
    

    #view the columns in our processed data frame using a for loop
    print("Columns in the data:")
    for column in data.columns: print('\t'+column)

    #some estimators allow us to provide the list of possible states an attribute can take
    #if not list is provided, the estimator assumes that all possible states are reflected in the data
    #you can provide the state names for all attributes, none of the attributes, or a subset of the attributes
    state_names = {}
    state_names['Smoking'] = [1,2,3,4,5,6,7,8]

    #Using expert input, create a list of known edges that MUST be included in the final structure
    fixed_edges = [("Smoking", "Level"),
                    #...add other known edges
    ]

    #Using expert input, create a list of forbidden edges that are FORBIDDEN from the final structure
    black_list = [("Alcohol Use", "Air Pollution"),
                    #...add other forbidden edges
    ]

    #choose a scoring method
    scoring_options = ['k2score', 'bdeuscore', 'bdsscore', 'bicscore', 'aicscore']
    scoring_method = scoring_options[3]

    #calling the hill climb estimator
    print("Estimating the model using hill climb search")
    hill_climb_model = learn_with_hillclimb(data=data, scoring_method=scoring_method,fixed_edges=fixed_edges, black_list=black_list)
    draw_bbn(hill_climb_model,"./output/hill_climb_"+scoring_method+".png")


    #calling the min max hill climb estimator
    #print("Estimating the model using min max hill climb search")
    #mmhc_model = learn_with_mmhc(data=data)


if __name__ == main():
    main()