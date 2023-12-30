import math
import unittest

import numpy as np


class Neuron:
    # Don't change anything in the `__init__` function.
    def __init__(self, examples):
        np.random.seed(42)
        # Three weights: one for each feature and one more for the bias.
        self.weights = np.random.normal(0, 1, 3 + 1)
        self.examples = examples
        self.train()

    # Don't use regularization.
    # Use mini-batch gradient descent.
    # Use the sigmoid activation function.
    # Use the defaults for the function arguments.
    def train(self, learning_rate=0.01, batch_size=10, epochs=200):
        # create some matrixes
        features_matrix = np.matrix([example["features"] for example in self.examples])
        labels_matrix = np.matrix([example["label"] for example in self.examples]).T
        # add bias
        features_matrix = np.insert(features_matrix, 3, 0, axis=1)

        # We got to go through all epochs
        for epoch in range(epochs):
            # For each epoch, grab random the minibatch
            previous_index = 0
            next_index = batch_size
            while next_index <= len(self.examples):
                np.random.shuffle(features_matrix)
                np.random.shuffle(labels_matrix)
                features_mb = features_matrix[previous_index:next_index]
                labels_mb = labels_matrix[previous_index:next_index]
                previous_index += batch_size
                next_index += batch_size
                # Multiply features x weighs
                matrix_mult = features_mb @ self.weights

                y_hat = self.sigmoid(matrix_mult)
                # Calculate loss function
                loss = self.cross_entropy(labels_mb.T, y_hat)
                print("Loss for epoch "+str(epoch)+": "+str(loss))

                # calculate the gradients per weigh i
                gradients = self.__find_gradients(features_mb, labels_mb.T, y_hat)
                self.weights = self.weights - learning_rate*gradients
                continue



    @staticmethod
    def sigmoid(value):
        return 1/(1 + np.exp(-value))

    @staticmethod
    def cross_entropy(y, y_hat):
        fp = y @ np.log(y_hat.T) + (1 - y_hat)
        return fp @ np.log(1 - y_hat).T

    def __find_gradients(self, features, labels, predictions):
        gradient = ((labels - predictions) @ features)/len(predictions)
        return gradient

    # Return the probability—not the corresponding 0 or 1 label.
    def predict(self, features):
        # Write your code here.
        pass




class TestingCases(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestingCases, self).__init__(*args, **kwargs)
        self.neuron = Neuron([{'features': [0.7737498370415932, 0.893981580520576, 0.7776116731845149], 'label': 0}, {'features': [0.8356527294792708, 0.7535044575176968, 0.7940884252881397], 'label': 0}, {'features': [0.8066217554804018, 0.863578574493143, 0.8610858626987106], 'label': 0}, {'features': [0.1306988673304761, 0.1917153596934752, 0.24189227746362746], 'label': 1}, {'features': [0.8272185404924335, 0.7036398824762223, 0.8573449106402691], 'label': 0}, {'features': [0.15396038670752804, 0.1833871954246849, 0.40843435733319716], 'label': 1}, {'features': [0.4092131679071596, 0.18153584517966398, 0.2572593518637127], 'label': 1}, {'features': [0.14459527809738992, 0.3032926767659022, 0.02400307776205829], 'label': 1}, {'features': [0.7352105415014727, 0.6788594540475846, 0.6824993122263854], 'label': 0}, {'features': [0.8463631632589925, 0.7549085251830376, 0.8476838061047185], 'label': 0}, {'features': [0.3123806898680401, 0.27342259758876564, 0.26882090734106606], 'label': 1}, {'features': [0.15098713351755333, 0.27267955662333865, 0.35682738600656144], 'label': 1}, {'features': [0.26599646550378536, 0.3078993496341542, 0.3641614601224931], 'label': 1}, {'features': [0.41664694240801076, 0.2920462871729351, 0.27249010027270154], 'label': 1}, {'features': [0.24358703392083086, 0.10140975843961991, 0.24867238584950097], 'label': 1}, {'features': [0.8276686654880372, 0.5631462965882309, 0.7901122630588067], 'label': 0}, {'features': [0.7538548484247882, 0.7563493662179133, 0.9060558868954207], 'label': 0}, {'features': [0.653114181642543, 0.8281988679600207, 0.8422663741740477], 'label': 0}, {'features': [0.9024360407961944, 0.7689309893630931, 0.655683007052765], 'label': 0}, {'features': [0.7476350559410989, 0.7662173389593208, 0.8889443916592481], 'label': 0}, {'features': [0.7006767267453662, 0.8465267101165077, 0.7854726735699382], 'label': 0}, {'features': [0.18372444356578327, 0.15209736911568922, 0.17865480622966], 'label': 1}, {'features': [0.25835793676162827, 0.2166447564607853, 0.5066866046843734], 'label': 1}, {'features': [0.34848185391755987, 0.15010261370695727, 0.3466287718524547], 'label': 1}, {'features': [0.27895696192284775, 0.25265158214739736, 0.34398276299698644], 'label': 1}, {'features': [0.2780075443127296, 0.2098453116059057, 0.360030710787324], 'label': 1}, {'features': [0.8175458435078011, 0.8649332061665285, 0.708315368552676], 'label': 0}, {'features': [0.7482586514165206, 0.5676772846686672, 0.8285473448226306], 'label': 0}, {'features': [0.14929738128165287, 0.24038371521478663, 0.1817006406305518], 'label': 1}, {'features': [0.1619272369177172, 0.03242763000417215, 0.22957349767604368], 'label': 1}, {'features': [0.27781127996430827, 0.3529944207096596, 0.10718241102563675], 'label': 1}, {'features': [0.7473036290862018, 0.8207366436085437, 0.6083439582203318], 'label': 0}, {'features': [0.13417467211657513, 0.267824191391427, 0.3092829850728432], 'label': 1}, {'features': [0.18746520892344104, 0.2793028361376617, 0.30328549427966606], 'label': 1}, {'features': [0.7206040216180081, 0.9927330347919765, 0.6987960226012109], 'label': 0}, {'features': [0.24652977738145104, 0.3104644425394525, 0.31713840092325213], 'label': 1}, {'features': [0.0, 0.43527803633710804, 0.2461393156706711], 'label': 1}, {'features': [0.7711144014334586, 0.7735558497059809, 0.8255237941816882], 'label': 0}, {'features': [0.07024853593410102, 0.3451823730559096, 0.2199802758785045], 'label': 1}, {'features': [0.14241976858622468, 0.4064226925135188, 0.3100039767465526], 'label': 1}, {'features': [0.714768255921445, 0.7144650319369523, 0.7237010638805477], 'label': 0}, {'features': [0.2519791780052621, 0.15418194548705366, 0.25407691543210204], 'label': 1}, {'features': [0.578219674955953, 0.8921712219951827, 0.8589198549785848], 'label': 0}, {'features': [0.31094952682691507, 0.2019227488114516, 0.29778178031111296], 'label': 1}, {'features': [0.18085163135017285, 0.11691689876440703, 0.26693267279250493], 'label': 1}, {'features': [0.006607663574594302, 0.22693494656499158, 0.31796705324985547], 'label': 1}, {'features': [1.0, 0.6426063333528218, 0.8621124372664304], 'label': 0}, {'features': [0.07272548773462939, 0.29788629023109214, 0.2872618508378623], 'label': 1}, {'features': [0.22026663038979716, 0.10577770516355278, 0.1068510651961192], 'label': 1}, {'features': [0.848398171298733, 0.7977520783375558, 0.9298663892303809], 'label': 0}, {'features': [0.09266724043329794, 0.27901615686267833, 0.20158443534815934], 'label': 1}, {'features': [0.8316789663279791, 0.883011611767281, 0.834489863437216], 'label': 0}, {'features': [0.8273755294557901, 0.8200796172371458, 0.578271319312857], 'label': 0}, {'features': [0.7480272870216644, 0.776817589610467, 0.7279244423030242], 'label': 0}, {'features': [0.877800016240931, 0.7170844286594831, 0.8927485210998554], 'label': 0}, {'features': [0.25041587118981373, 0.10492495981715594, 0.36757797220418903], 'label': 1}, {'features': [0.7886985158760524, 0.6359002367782174, 0.8135112644560474], 'label': 0}, {'features': [0.021347826993614316, 0.08173787358191598, 0.2862410700874736], 'label': 1}, {'features': [0.8354050233064492, 0.8068807245679099, 0.9329294787827505], 'label': 0}, {'features': [0.27485180221367306, 0.3850464089660449, 0.2363355193471532], 'label': 1}, {'features': [0.07348365922334715, 0.3013062328344346, 0.21930855061272397], 'label': 1}, {'features': [0.14406656489504605, 0.19881690454595385, 0.1679376861489939], 'label': 1}, {'features': [0.6068888431790089, 0.8437721144091828, 0.7330710439653292], 'label': 0}, {'features': [0.7888110926492717, 0.7470303168346561, 0.8645158415663305], 'label': 0}, {'features': [0.7385371726196368, 0.8119236926611204, 0.7001067747114078], 'label': 0}, {'features': [0.34890474846396896, 0.30820854058619285, 0.162830490539224], 'label': 1}, {'features': [0.32650807444328284, 0.20460174856922125, 0.20949113958734433], 'label': 1}, {'features': [0.7447843282845086, 0.6331399345750838, 0.5912651308343988], 'label': 0}, {'features': [0.9398432075332075, 0.6741954276106651, 0.8164719709786763], 'label': 0}, {'features': [0.2828546775066982, 0.3765925942357281, 0.2135121537082179], 'label': 1}, {'features': [0.9316479949484426, 0.9482775048779457, 0.8738120310808861], 'label': 0}, {'features': [0.908866922189042, 0.7484615200627229, 0.8280016643917809], 'label': 0}, {'features': [0.1354773111272577, 0.35168497006775346, 0.26815684551322], 'label': 1}, {'features': [0.7221146373384091, 0.7055622946733191, 0.8334399172111424], 'label': 0}, {'features': [0.2365362147632843, 0.269049237819466, 0.31989149150619706], 'label': 1}, {'features': [0.7656394675139337, 0.6878555384927062, 1.0], 'label': 0}, {'features': [0.8045141910141134, 0.6875135456954657, 0.7758856060333839], 'label': 0}, {'features': [0.6769137431398171, 0.8369178788929816, 0.8897321901753998], 'label': 0}, {'features': [0.648553375777358, 0.8780545567511548, 0.8142310125935506], 'label': 0}, {'features': [0.15984932429383653, 0.0, 0.12547018008207195], 'label': 1}, {'features': [0.7534430946256954, 0.8778345528133455, 0.9128314938981439], 'label': 0}, {'features': [0.16949532079803759, 0.3663306568091933, 0.38322997790498464], 'label': 1}, {'features': [0.13841065464487234, 0.31093608814592677, 0.1619175592785912], 'label': 1}, {'features': [0.7245058154497992, 0.8860469048223394, 0.8128459509662227], 'label': 0}, {'features': [0.5919600245879655, 0.7824558267672665, 0.9484723762808895], 'label': 0}, {'features': [0.9389493797739454, 0.8295552014744696, 0.8449851289455774], 'label': 0}, {'features': [0.3962831333121017, 0.061828564376677386, 0.2687627247961932], 'label': 1}, {'features': [0.16323132687083614, 0.23372591991661418, 0.11222931228194033], 'label': 1}, {'features': [0.7911423015097825, 0.773843674993097, 0.8182473210747465], 'label': 0}, {'features': [0.2685831591581727, 0.3257074269653475, 0.45382357924788547], 'label': 1}, {'features': [0.632296178216958, 0.7689048519640287, 0.8790566188829325], 'label': 0}, {'features': [0.612856125708396, 1.0, 0.7356878286469197], 'label': 0}, {'features': [0.2684032384079434, 0.2485146958025073, 0.12661015461253344], 'label': 1}, {'features': [0.16478464089656814, 0.24560650799180528, 0.0], 'label': 1}, {'features': [0.30824344058078407, 0.22912485105738056, 0.1957281914191144], 'label': 1}, {'features': [0.840370119369737, 0.8315454791763808, 0.8681720716363501], 'label': 0}, {'features': [0.9063726499357183, 0.7314201058403522, 0.8217554110088645], 'label': 0}, {'features': [0.28146402235173357, 0.32730110688021274, 0.2595902873226133], 'label': 1}, {'features': [0.9937932184850524, 0.8732955188203595, 0.9268163245204615], 'label': 0}, {'features': [0.7277102704753939, 0.8570915764071192, 0.7868840674025182], 'label': 0}])

    def test_case_1(self):
        expected = 0.1636
        actual = self.neuron.predict([0.79, 0.89, 0.777])
        self.assertEqual(self.__round_to_4(actual), expected)

    def test_case_2(self):
        expected = 0.1551
        actual = self.neuron.predict([0.8066217554804018, 0.863578574493143, 0.8610858626987106])
        self.assertEqual(self.__round_to_4(actual), expected)

    def test_case_3(self):
        expected = 0.331
        actual = self.neuron.predict([0.7, 0.6, 0.5])
        self.assertEqual(self.__round_to_4(actual), expected)

    def test_case_4(self):
        expected = 0.7287
        actual = self.neuron.predict([0.1, 0.2, 0.3])
        self.assertEqual(self.__round_to_4(actual), expected)

    def test_case_5(self):
        expected = 0.64
        actual = self.neuron.predict([0.2, 0.3, 0.4])
        self.assertEqual(self.__round_to_4(actual), expected)

    def test_case_6(self):
        expected = 0.9684
        actual = self.neuron.predict([-0.3, -0.4, -0.5])
        self.assertEqual(self.__round_to_4(actual), expected)

    def __round_to_4(self, number):
        if not self.__is_number(number):
            # Bad output; let tests fail.
            return number

        return round(number, 4)

    def __is_number(self, element):
        return type(element) in (int, float)


if __name__ == '__main__':
    unittest.main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
