# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class SplitPoint:
    def __init__(self, feature, value):
        self.feature = feature
        self.value = value


class TreeNode:
    def __init__(self, examples):
        self.examples = examples
        self.left = None
        self.right = None
        self.split_point = None

    def split(self):
        min_mse = float("inf")
        features = list(self.examples[0].keys())[:-1]
        final_split_feature = features[0]
        final_split_value = None
        for feature in features:
            # get all the values for current feature
            sorted_feature_values = [example[feature] for example in self.examples]
            # sort all the values for current feature
            sorted_feature_values = sorted(sorted_feature_values)
            #  calculating possible split values
            possible_split_value_for_current_feature = [(sorted_feature_values[i] + sorted_feature_values[i + 1]) / 2
                                                         for i in range(len(sorted_feature_values) - 1)]
            if len(possible_split_value_for_current_feature) == 0:
                # can't split anymore
                return
            # calculate mse per split and store in dict = {split_value: mse}
            mse_per_split_value_for_current_feature = {
                split_value_for_current_feature: self.__get_mse_per_split(split_value_for_current_feature, feature)
                for split_value_for_current_feature in possible_split_value_for_current_feature
            }

            # get the min mse
            sorted_mse_per_split_point_for_current_feature = sorted(mse_per_split_value_for_current_feature.items(),
                                                                    key=lambda x: x[1])

            # set the splitting criteria based on min mse
            if sorted_mse_per_split_point_for_current_feature[0][1] < min_mse:
                min_mse = sorted_mse_per_split_point_for_current_feature[0][1]
                final_split_feature = feature
                final_split_value = sorted_mse_per_split_point_for_current_feature[0][0]
                self.split_point = SplitPoint(feature, sorted_mse_per_split_point_for_current_feature[0][0])

        # populate left and right based on criteria
        self.left = TreeNode([example for example in self.examples if example[final_split_feature] < final_split_value])
        self.right = TreeNode(
            [example for example in self.examples if example[final_split_feature] >= final_split_value])

        # check if we should stop splitting
        if self.left.examples is None or self.right.examples is None:
            return

        self.left.split()
        self.right.split()

    def __get_mse_per_split(self, split_value_for_current_feature, feature):
        left_examples = [example for example in self.examples if example[feature] < split_value_for_current_feature]
        right_examples = [example for example in self.examples if example[feature] >= split_value_for_current_feature]
        average_left = sum([example["bpd"] for example in left_examples]) / len(left_examples)
        average_right = sum([example["bpd"] for example in right_examples]) / len(right_examples)
        mse_left = sum([(example["bpd"] - average_left) ** 2 for example in left_examples])
        mse_right = sum([(example["bpd"] - average_right) ** 2 for example in right_examples])
        return (mse_left + mse_right) / (len(left_examples) + len(right_examples))


class RegressionTree:
    def __init__(self, examples):
        # Don't change the following two lines of code.
        self.root = TreeNode(examples)
        self.train()

    def train(self):
        # Don't edit this line.
        self.root.split()

    def predict(self, example):
        return self.__predict(example, self.root)

    def __predict(self, example, node):
        if node.left is None or node.right is None:
            # leaf node
            nominator = sum([node['bpd'] for node in node.examples])
            denominator = len(node.examples)
            return float(nominator/denominator)
        node_feature = node.split_point.feature
        node_value = node.split_point.value
        if example[node_feature] < node_value:
            return self.__predict(example, node.left)
        else:
            return self.__predict(example, node.right)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    training_data = [{'porosity': 0.3371143747544963, 'gamma': 1.5532281763256406, 'sonic': 2688.3982231067453,
                      'density': 2.3844675358491108, 'bpd': 267.368493934757},
                     {'porosity': 0.4337347720759379, 'gamma': 1.4919437732469303, 'sonic': 2951.9393570543866,
                      'density': 3.3225004830628286, 'bpd': 137.92769419082313},
                     {'porosity': 0.7841412874659546, 'gamma': 1.4641354059830916, 'sonic': 3292.528322692423,
                      'density': 2.9454048576245238, 'bpd': 94.39862604475096},
                     {'porosity': 0.6674049348861592, 'gamma': 1.7114534905779109, 'sonic': 3026.7244582466697,
                      'density': 4.00567135123098, 'bpd': 570.4559270159473},
                     {'porosity': 0.5055073697777869, 'gamma': 1.5799489627951153, 'sonic': 2248.1340040091864,
                      'density': 3.1545176915064994, 'bpd': 336.61734627973374},
                     {'porosity': 0.5977806969539097, 'gamma': 1.4956784664056788, 'sonic': 2851.422913577109,
                      'density': 3.986503026689371, 'bpd': 131.15785568859494},
                     {'porosity': 0.38349450754274095, 'gamma': 1.5119377760558304, 'sonic': 3107.4259242789553,
                      'density': 1.8491373941315696, 'bpd': 166.61190357625637},
                     {'porosity': 0.6493353063806808, 'gamma': 1.660919515440599, 'sonic': 2873.186436121522,
                      'density': 2.8277602660669396, 'bpd': 426.3599050094518},
                     {'porosity': 0.5148238392941548, 'gamma': 1.8428789115155966, 'sonic': 3477.3492315202907,
                      'density': 1.6570540426940608, 'bpd': 115.17964587339662},
                     {'porosity': 0.6354277817086049, 'gamma': 1.581797989427644, 'sonic': 2571.9575874329894,
                      'density': 2.326889350644146, 'bpd': 396.5070591933734},
                     {'porosity': 0.5718721746302671, 'gamma': 1.372854959321451, 'sonic': 3538.467028856794,
                      'density': 1.6920987581448308, 'bpd': 197.8710452592074},
                     {'porosity': 0.6245306427184388, 'gamma': 1.5714665989534873, 'sonic': 2685.3737054790167,
                      'density': 2.721659007061907, 'bpd': 111.30413842080821},
                     {'porosity': 0.790284293091575, 'gamma': 1.3882208475753202, 'sonic': 2306.3707831653664,
                      'density': 3.1661953451919835, 'bpd': 116.41540672016879},
                     {'porosity': 0.058672948847231135, 'gamma': 1.5384704880812365, 'sonic': 3236.794545516582,
                      'density': 1.2698807135982118, 'bpd': 159.49129568528647},
                     {'porosity': 0.6184198610596466, 'gamma': 1.506808073915736, 'sonic': 2353.0200391181215,
                      'density': 2.663854871691728, 'bpd': 303.2829972469314},
                     {'porosity': 0.5440789737306038, 'gamma': 1.6127637672530575, 'sonic': 1906.0799417773328,
                      'density': 2.513776213138042, 'bpd': 246.02946840651651},
                     {'porosity': 0.24230826038076003, 'gamma': 1.5600463819136288, 'sonic': 2568.8231147730116,
                      'density': -0.353639698833012, 'bpd': 164.7544334411493},
                     {'porosity': 0.10616919455679025, 'gamma': 1.71362086458076, 'sonic': 3345.428222547903,
                      'density': 3.184405678567027, 'bpd': 202.03418116076776},
                     {'porosity': 0.545608405366316, 'gamma': 1.3926083533517064, 'sonic': 3984.0780802808226,
                      'density': 3.194688232879604, 'bpd': 134.89623324778916},
                     {'porosity': 0.5830763419832076, 'gamma': 1.5149175738662581, 'sonic': 3179.700666729194,
                      'density': 3.102824301029373, 'bpd': 282.9415619667002},
                     {'porosity': 0.5436396082774595, 'gamma': 1.5500878587300029, 'sonic': 2183.308367015772,
                      'density': 3.166385158753267, 'bpd': 325.2208059909965},
                     {'porosity': 0.5305613081991847, 'gamma': 1.6446397533367605, 'sonic': 3432.885963765256,
                      'density': 2.8059408226891955, 'bpd': 75.55511378122458},
                     {'porosity': 0.09908051122638568, 'gamma': 1.3662892151595505, 'sonic': 3542.3499660514417,
                      'density': 2.0994789717922564, 'bpd': 187.81212733429916},
                     {'porosity': 0.32446853348269605, 'gamma': 1.4600481331675748, 'sonic': 1652.675795106473,
                      'density': 1.7983076095774595, 'bpd': 185.45312294552565},
                     {'porosity': 0.7562004411662702, 'gamma': 1.5534121123070688, 'sonic': 3359.2311531852793,
                      'density': 3.2791554780745913, 'bpd': 143.06979013832327},
                     {'porosity': 0.4291669345977492, 'gamma': 1.601626763055697, 'sonic': 2385.722794854003,
                      'density': 2.605002774849955, 'bpd': 223.75411474737294},
                     {'porosity': 0.5147032855542052, 'gamma': 1.47174128573156, 'sonic': 2529.717382783449,
                      'density': 3.550539771530782, 'bpd': 368.16830244258523},
                     {'porosity': 0.5494848015255834, 'gamma': 1.572683602433637, 'sonic': 3719.4054023785006,
                      'density': 3.012187857465139, 'bpd': 122.77635789491812},
                     {'porosity': 0.30554754246069804, 'gamma': 1.5600407755884875, 'sonic': 4416.89932949216,
                      'density': 2.722556268713408, 'bpd': 212.14065437198585},
                     {'porosity': 0.7741653370614074, 'gamma': 1.5581707001397844, 'sonic': 2306.3705139840304,
                      'density': 1.8470217546212844, 'bpd': 317.59594616902433},
                     {'porosity': 0.29396153999324925, 'gamma': 1.6085862165361424, 'sonic': 2243.470743239841,
                      'density': 2.4799889898217145, 'bpd': 251.78064784405683},
                     {'porosity': 0.5456855132240469, 'gamma': 1.7669919850037175, 'sonic': 3027.1308690533015,
                      'density': 3.7205542817199033, 'bpd': 95.89186084404717},
                     {'porosity': 0.6361425899136316, 'gamma': 1.556617694292124, 'sonic': 3119.050366673754,
                      'density': 2.471696998199376, 'bpd': 142.76565405442182},
                     {'porosity': 0.619711520752428, 'gamma': 1.698799769269184, 'sonic': 2605.4531834652785,
                      'density': 3.409158931098213, 'bpd': 152.97422355163644},
                     {'porosity': 0.5072289686210225, 'gamma': 1.4617503462982175, 'sonic': 2049.004323276818,
                      'density': 2.1977543054778668, 'bpd': 155.36582712758062},
                     {'porosity': 0.6168721986290795, 'gamma': 1.582459489456767, 'sonic': 3444.43856884036,
                      'density': 3.6949446558893753, 'bpd': 457.12366221396275},
                     {'porosity': 0.5829984052902517, 'gamma': 1.5281946214243451, 'sonic': 3007.921064337612,
                      'density': 3.8233140986510663, 'bpd': 92.61721887385505},
                     {'porosity': 0.5589820092733596, 'gamma': 1.6437766904184952, 'sonic': 3195.838829757016,
                      'density': 2.4275153842454653, 'bpd': 152.70553729464697},
                     {'porosity': 0.5851175708008849, 'gamma': 1.5371516939215863, 'sonic': 2964.6623620013047,
                      'density': 2.696298833367787, 'bpd': 110.55308777960273},
                     {'porosity': 0.46172198043650325, 'gamma': 1.5938365329762796, 'sonic': 3047.9008432966216,
                      'density': 3.1397063718564464, 'bpd': 283.71685694500906},
                     {'porosity': 0.2617493207329127, 'gamma': 1.5857031392768857, 'sonic': 2072.728704616695,
                      'density': 1.4296201309623835, 'bpd': 200.85265603095922},
                     {'porosity': 0.6007532428818765, 'gamma': 1.5056356949883916, 'sonic': 1721.7628916426506,
                      'density': 3.459458156582599, 'bpd': 135.9979736710587},
                     {'porosity': 0.5836251475889298, 'gamma': 1.4942000015651398, 'sonic': 1971.5336209943118,
                      'density': 2.8449423053344014, 'bpd': 471.0066130521506},
                     {'porosity': 0.6512588271004689, 'gamma': 1.5195256378740227, 'sonic': 3287.983336916015,
                      'density': 3.21869662371343, 'bpd': 99.08117863596135},
                     {'porosity': 0.684298338288051, 'gamma': 1.4584945220756098, 'sonic': 1785.468686765673,
                      'density': 3.522181155485258, 'bpd': 316.8571404163882},
                     {'porosity': 0.3575931092573688, 'gamma': 1.384558404094262, 'sonic': 3235.7804354908494,
                      'density': 2.4815421153252273, 'bpd': 264.9998032825209},
                     {'porosity': 0.3173979487685147, 'gamma': 1.7210318450974702, 'sonic': 2805.661187646785,
                      'density': 2.3126370008712156, 'bpd': 222.5560489973494},
                     {'porosity': 0.4881924480770495, 'gamma': 1.4852168141882707, 'sonic': 2624.8027428526125,
                      'density': 3.259626335377611, 'bpd': 61.14391444494984},
                     {'porosity': 0.4599404841248312, 'gamma': 1.5717748080576657, 'sonic': 2529.71663948199,
                      'density': 1.5193761030290385, 'bpd': 208.62018210107695},
                     {'porosity': 0.34376292232981526, 'gamma': 1.7025464694292771, 'sonic': 3215.761012617203,
                      'density': 2.0771641271369283, 'bpd': 182.3732003355993},
                     {'porosity': 0.6513153743868741, 'gamma': 1.63636611843326, 'sonic': 3875.3188177227294,
                      'density': 4.005633553870243, 'bpd': 139.74790497198032},
                     {'porosity': 0.7942622592732644, 'gamma': 1.5870471834794628, 'sonic': 3790.30612492106,
                      'density': 3.8315414441943547, 'bpd': 121.94323012420132},
                     {'porosity': 0.34593718470715273, 'gamma': 1.4014335854402913, 'sonic': 2418.5879016289764,
                      'density': 1.380519373848317, 'bpd': 191.19747307323144},
                     {'porosity': 0.5180657621946733, 'gamma': 1.4909410629295659, 'sonic': 2769.1640297922886,
                      'density': 2.120040953804959, 'bpd': 293.0667742514089},
                     {'porosity': 0.4185792240376649, 'gamma': 1.6473648033357478, 'sonic': 2581.609497748305,
                      'density': 2.3905913965904477, 'bpd': 214.26501469194866},
                     {'porosity': 0.3882192804589885, 'gamma': 1.5618215545690952, 'sonic': 3426.9357888704726,
                      'density': 2.628989049423201, 'bpd': 229.74961854025847},
                     {'porosity': 0.4914863989448688, 'gamma': 1.4933142574786205, 'sonic': 3049.652713850185,
                      'density': 2.286755870656806, 'bpd': 210.6635906695101},
                     {'porosity': 0.5386553876138837, 'gamma': 1.5165015145554754, 'sonic': 1516.191867529383,
                      'density': 3.2611103463766966, 'bpd': 412.19932077217993},
                     {'porosity': 0.309397160487144, 'gamma': 1.5896073368969483, 'sonic': 2982.0396301355763,
                      'density': 2.885430734587411, 'bpd': 267.62129152827896},
                     {'porosity': 0.6276993677335759, 'gamma': 1.5314310790107206, 'sonic': 2213.9695782498807,
                      'density': 2.873147118420167, 'bpd': 370.3270671853462},
                     {'porosity': 0.48460940514062656, 'gamma': 1.4365118509210983, 'sonic': 3372.992041867824,
                      'density': 2.3660271437532976, 'bpd': 254.6345527580149},
                     {'porosity': 0.3828267569312653, 'gamma': 1.6751491520041815, 'sonic': 2201.5318699111344,
                      'density': 2.1857320272167704, 'bpd': 196.0150083063314},
                     {'porosity': 0.20900186962779038, 'gamma': 1.6196056724251195, 'sonic': 3403.32361226404,
                      'density': 1.6034572944997816, 'bpd': 160.63589373537806},
                     {'porosity': 0.6003717038389424, 'gamma': 1.6383485293440867, 'sonic': 3165.4136780505846,
                      'density': 3.5287373017778783, 'bpd': 335.6610208771159},
                     {'porosity': 0.6516171780138297, 'gamma': 1.4740428927547997, 'sonic': 2779.079394371239,
                      'density': 2.585706429715077, 'bpd': 95.10970235158351},
                     {'porosity': 0.4310704613032884, 'gamma': 1.5788529102959974, 'sonic': 1878.4589668663436,
                      'density': 2.6660019003367856, 'bpd': 235.8879404569585},
                     {'porosity': 0.68278039443353, 'gamma': 1.671330510224613, 'sonic': 2957.8347455861667,
                      'density': 3.158624750603302, 'bpd': 249.4841228954935},
                     {'porosity': 0.4406191221114598, 'gamma': 1.6920678057370027, 'sonic': 2306.01143815942,
                      'density': 2.9755234750728947, 'bpd': 389.34501132787625},
                     {'porosity': 0.6052805491229261, 'gamma': 1.7743369462465957, 'sonic': 3275.7692973373396,
                      'density': 3.0338661485091416, 'bpd': 110.86228190122422},
                     {'porosity': 0.27106383466754985, 'gamma': 1.7571394619831942, 'sonic': 2628.1636577312534,
                      'density': 3.271627759706612, 'bpd': 120.27393550466441},
                     {'porosity': 0.507433883020902, 'gamma': 1.5896210519278267, 'sonic': 2267.0820269445085,
                      'density': 2.450308600843854, 'bpd': 253.9357841999945},
                     {'porosity': 0.3553407007132533, 'gamma': 1.4325098030593038, 'sonic': 2628.8235774679138,
                      'density': 1.7200150981971043, 'bpd': 164.57428725951036},
                     {'porosity': 0.4926996158892533, 'gamma': 1.532734190407079, 'sonic': 2347.941529496951,
                      'density': 2.8886743145592297, 'bpd': 386.9583414198195},
                     {'porosity': 0.567287061238642, 'gamma': 1.5897043180449646, 'sonic': 2517.9215277391163,
                      'density': 3.3912331783788723, 'bpd': 382.6168230908595},
                     {'porosity': 0.38472161774882024, 'gamma': 1.3819566048282528, 'sonic': 2214.2956519624677,
                      'density': 2.1292205455062545, 'bpd': 217.30413793749733},
                     {'porosity': 0.8094499226230966, 'gamma': 1.6869172186864432, 'sonic': 3085.7552603394397,
                      'density': 3.0347630523236466, 'bpd': 816.9979427612899},
                     {'porosity': 0.5882398102858528, 'gamma': 1.6106431239211796, 'sonic': 3108.0623128768357,
                      'density': 3.5700315284312345, 'bpd': 104.51710529990538},
                     {'porosity': 0.5175400158449357, 'gamma': 1.6290422407111742, 'sonic': 3161.841799030992,
                      'density': 3.2298109652145457, 'bpd': 140.0522300706841},
                     {'porosity': 0.8294144222546056, 'gamma': 1.5407362261508322, 'sonic': 3737.64748537745,
                      'density': 2.5681797403952222, 'bpd': 141.8764577589994},
                     {'porosity': 0.37047743145150025, 'gamma': 1.6577334482231394, 'sonic': 2457.2151990368093,
                      'density': 2.4718329087713857, 'bpd': 200.13035118308574},
                     {'porosity': 0.40230756530764805, 'gamma': 1.3997841635125337, 'sonic': 1505.2503215988995,
                      'density': 2.1872763744242074, 'bpd': 507.5805808408982},
                     {'porosity': 0.7475291305449694, 'gamma': 1.4618781276234905, 'sonic': 3128.3238024200027,
                      'density': 2.952485361620549, 'bpd': 151.87145316772265},
                     {'porosity': 0.4821959432320581, 'gamma': 1.4953123610344377, 'sonic': 2768.866560695128,
                      'density': 1.1231264377284371, 'bpd': 157.33821193599536},
                     {'porosity': 0.6302967631883345, 'gamma': 1.4535774127048533, 'sonic': 2727.3468601139803,
                      'density': 2.6691242584517996, 'bpd': 333.76782259121535},
                     {'porosity': 0.5707713867465943, 'gamma': 1.4240205479646413, 'sonic': 2996.5541542212786,
                      'density': 2.124091581527941, 'bpd': 342.07262722524706},
                     {'porosity': 0.6881491112241366, 'gamma': 1.6334729728200879, 'sonic': 3682.906973237694,
                      'density': 3.0070391869540125, 'bpd': 154.2088521609673},
                     {'porosity': 0.6978386794352496, 'gamma': 1.4750840322950738, 'sonic': 2621.181900650031,
                      'density': 1.3600123594556799, 'bpd': 113.15359444368231},
                     {'porosity': 0.5346115424047748, 'gamma': 1.6109264094688156, 'sonic': 2013.9922327579163,
                      'density': 2.92859864226241, 'bpd': 123.19723727372079},
                     {'porosity': 0.3658264424093018, 'gamma': 1.5559217363439988, 'sonic': 2750.4072846395206,
                      'density': 2.109555962577691, 'bpd': 209.12616838607002},
                     {'porosity': 0.36329966027788935, 'gamma': 1.58213136421782, 'sonic': 2895.485201774988,
                      'density': 2.950276113611119, 'bpd': 209.80812614883328},
                     {'porosity': 0.4320474601690374, 'gamma': 1.5483961166697728, 'sonic': 2934.4543717618867,
                      'density': 2.994802186669173, 'bpd': 246.75749559971854},
                     {'porosity': 0.6889796005189635, 'gamma': 1.4703738676757077, 'sonic': 2427.3846829110394,
                      'density': 3.9249237482174166, 'bpd': 420.40271723811645},
                     {'porosity': 0.49906384196939696, 'gamma': 1.5608694304594546, 'sonic': 2197.1613701050005,
                      'density': 3.0920550961192963, 'bpd': 435.8559184779223},
                     {'porosity': 0.7514088546574156, 'gamma': 1.5493175516919322, 'sonic': 2443.382129553198,
                      'density': 3.621307380152593, 'bpd': 319.9385277864086},
                     {'porosity': 0.43306016872787956, 'gamma': 1.4587637883283566, 'sonic': 2715.8176808810213,
                      'density': 3.5247607163750074, 'bpd': 260.96014238732386},
                     {'porosity': 0.4160974316111965, 'gamma': 1.5555740946927492, 'sonic': 3133.5867273653216,
                      'density': 1.3182187905626983, 'bpd': 171.8265844282526},
                     {'porosity': 0.4247852168523866, 'gamma': 1.5945988097430674, 'sonic': 3333.3919926123926,
                      'density': 2.9292265185180595, 'bpd': 122.56528595083694},
                     {'porosity': 0.6251334337449636, 'gamma': 1.580341891727447, 'sonic': 2194.526055442898,
                      'density': 3.7758255444858073, 'bpd': 361.98085109469827},
                     {'porosity': 0.4990632470818737, 'gamma': 1.5438290949723217, 'sonic': 3620.255563365596,
                      'density': 2.351919738897265, 'bpd': 178.41834444303797},
                     {'porosity': 0.7530128093276482, 'gamma': 1.6925458002746128, 'sonic': 2991.525096310008,
                      'density': 3.506978590208996, 'bpd': 534.8788389313542}]
    new_tree = RegressionTree(training_data)
    print(new_tree.predict({
        "density": 2.52,
        "gamma": 1.57,
        "porosity": 0.7,
        "sonic": 3666.9
    }))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
