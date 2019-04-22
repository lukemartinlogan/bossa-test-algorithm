
from TestData import *
from TestAlgorithm import *
from Visualize import *


def visualize():
	df = load_results("./results.csv")
	view_tests(df, building="SB", floor=1, day=None, bin_strategy=3, save_path="./SB_01_R.html", results=(0, 1000))
	
def test_alg():

	#Open the test cases for a certain building
	print("Opening test cases")
	cases = TestCases(out="sim_results.csv")
	cases.open_test_data(path="SimulatedData.csv", building="SB")
	
	#Run the original bins over the new test data
	print("Testing original bin strategy")
	cases.test_algorithm(loc_alg = 2, floor_alg = 1, bin_strategy = 2)
	cases.to_csv()
	
	#Run the new bins over the new test data
	print("Testing new bin strategy")
	cases.test_algorithm(loc_alg = 2, floor_alg = 1, bin_strategy = 3)
	cases.to_csv()

def optimize_bins():

	#Open the test cases for a certain building
	print("Opening test cases")
	cases = TestCases()
	cases.open_test_data(building="SB", floor=1)
	
	#Run the new bins over the new test data
	print("Optimizing Bins")
	cases.optimize_bins(loc_alg=2, floor_alg=1, top_n=3, num_guesses = 20)

def main():
	test_alg()

if __name__ == "__main__":
	main()

	
	
	