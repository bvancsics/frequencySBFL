import algorithms


# four_bool_vector=[ef, ep, nf, np])

class SorensenDice(algorithms.Algorithm):
    def init_score(self, methodNames):
        self.score = {}
        for m in methodNames:
            self.score[m] = 0.0

    def calculation(self, methodNames, current_four_metrics=None, w_current_four_metrics=None, four_bool_vector=None, numerator_ef=False):
        for method in methodNames:
            w_ef = None if numerator_ef is False else self.get_numerator_weighted_ef(method, w_current_four_metrics)
            ef, ep, nf, _np = self.get_act_four_metrics(method, current_four_metrics, w_current_four_metrics, four_bool_vector)
            self.score[method] = self.sorensen_dice(ef, ep, nf, w_ef)
        return self.score


    def call(self, metricName, methodNames, hit_results, unique_results, naive_results):
        self.init_score(methodNames)
        if metricName == "SorensenDice-hit":
            return self.calculation(methodNames,
                                    hit_results,
                                    None,
                                    [False, False, False, False])
        # ============================================================
        # ============================================================
        elif metricName == "SorensenDice-unique-num_ef":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [False, False, False, False],
                                    numerator_ef=True)
        elif metricName == "SorensenDice-unique-ef":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [True, False, False, False])
        elif metricName == "SorensenDice-unique-ep":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [False, True, False, False])
        elif metricName == "SorensenDice-unique-nf":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [False, False, True, False])
        elif metricName == "SorensenDice-unique-np":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [False, False, False, True])
        # --------------------------------
        elif metricName == "SorensenDice-unique-ef_ep":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [True, True, False, False])
        elif metricName == "SorensenDice-unique-ef_nf":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [True, False, True, False])
        elif metricName == "SorensenDice-unique-ef_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [True, False, False, True])
        elif metricName == "SorensenDice-unique-ep_nf":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [False, True, True, False])
        elif metricName == "SorensenDice-unique-ep_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [False, True, False, True])
        elif metricName == "SorensenDice-unique-nf_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [False, False, True, True])
        #--------------------------------
        elif metricName == "SorensenDice-unique-ef_ep_nf":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [True, True, True, False])
        elif metricName == "SorensenDice-unique-ef_ep_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [True, True, False, True])
        elif metricName == "SorensenDice-unique-ef_nf_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [True, False, True, True])
        elif metricName == "SorensenDice-unique-ep_nf_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [False, True, True, True])
        # --------------------------------
        elif metricName == "SorensenDice-unique-ef_ep_nf_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [True, True, True, True])
        # ============================================================
        # ============================================================
        elif metricName == "SorensenDice-naive-num_ef":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [False, False, False, False],
                                    numerator_ef=True)
        elif metricName == "SorensenDice-naive-ef":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [True, False, False, False])
        elif metricName == "SorensenDice-naive-ep":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [False, True, False, False])
        elif metricName == "SorensenDice-naive-nf":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [False, False, True, False])
        elif metricName == "SorensenDice-naive-np":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [False, False, False, True])
        # --------------------------------
        elif metricName == "SorensenDice-naive-ef_ep":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [True, True, False, False])
        elif metricName == "SorensenDice-naive-ef_nf":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [True, False, True, False])
        elif metricName == "SorensenDice-naive-ef_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [True, False, False, True])
        elif metricName == "SorensenDice-naive-ep_nf":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [False, True, True, False])
        elif metricName == "SorensenDice-naive-ep_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [False, True, False, True])

        elif metricName == "SorensenDice-naive-nf_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [False, False, True, True])
        #--------------------------------
        elif metricName == "SorensenDice-naive-ef_ep_nf":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [True, True, True, False])
        elif metricName == "SorensenDice-naive-ef_ep_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [True, True, False, True])
        elif metricName == "SorensenDice-naive-ef_nf_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [True, False, True, True])
        elif metricName == "SorensenDice-naive-ep_nf_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [False, True, True, True])
        # --------------------------------
        elif metricName == "SorensenDice-naive-ef_ep_nf_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [True, True, True, True])