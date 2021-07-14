import algorithms

# four_bool_vector=[ef, ep, nf, np])

class Barinel(algorithms.Algorithm):
    def init_score(self, methodNames):
        self.score = {}
        for m in methodNames:
            self.score[m] = 0.0

    def calculation(self, methodNames, current_four_metrics=None, w_current_four_metrics=None, four_bool_vector=None, numerator_ef=False):
        for method in methodNames:
            w_ef = None if numerator_ef is False else self.get_numerator_weighted_ef(method, w_current_four_metrics)
            ef, ep, _nf, _np = self.get_act_four_metrics(method, current_four_metrics, w_current_four_metrics, four_bool_vector)
            self.score[method] = self.barinel(ef, ep, w_ef)
        return self.score


    def call(self, metricName, methodNames, hit_results, unique_results, naive_results):
        self.init_score(methodNames)
        if metricName == "Barinel-hit":
            return self.calculation(methodNames,
                                    hit_results,
                                    None,
                                    [False, False, False, False])
        # ============================================================
        # ============================================================
        elif metricName == "Barinel-unique-num_ef":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [False, False, False, False],
                                    numerator_ef=True)
        elif metricName == "Barinel-unique-ef":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [True, False, False, False])
        elif metricName == "Barinel-unique-ep":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [False, True, False, False])
        elif metricName == "Barinel-unique-nf":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [False, False, True, False])
        elif metricName == "Barinel-unique-np":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [False, False, False, True])
        # --------------------------------
        elif metricName == "Barinel-unique-ef_ep":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [True, True, False, False])
        elif metricName == "Barinel-unique-ef_nf":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [True, False, True, False])
        elif metricName == "Barinel-unique-ef_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [True, False, False, True])
        elif metricName == "Barinel-unique-ep_nf":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [False, True, True, False])
        elif metricName == "Barinel-unique-ep_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [False, True, False, True])
        elif metricName == "Barinel-unique-nf_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [False, False, True, True])
        #--------------------------------
        elif metricName == "Barinel-unique-ef_ep_nf":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [True, True, True, False])
        elif metricName == "Barinel-unique-ef_ep_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [True, True, False, True])
        elif metricName == "Barinel-unique-ef_nf_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [True, False, True, True])
        elif metricName == "Barinel-unique-ep_nf_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [False, True, True, True])
        # --------------------------------
        elif metricName == "Barinel-unique-ef_ep_nf_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [True, True, True, True])
        # ============================================================
        # ============================================================
        elif metricName == "Barinel-naive-num_ef":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [False, False, False, False],
                                    numerator_ef=True)
        elif metricName == "Barinel-naive-ef":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [True, False, False, False])
        elif metricName == "Barinel-naive-ep":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [False, True, False, False])
        elif metricName == "Barinel-naive-nf":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [False, False, True, False])
        elif metricName == "Barinel-naive-np":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [False, False, False, True])
        # --------------------------------
        elif metricName == "Barinel-naive-ef_ep":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [True, True, False, False])
        elif metricName == "Barinel-naive-ef_nf":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [True, False, True, False])
        elif metricName == "Barinel-naive-ef_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [True, False, False, True])
        elif metricName == "Barinel-naive-ep_nf":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [False, True, True, False])
        elif metricName == "Barinel-naive-ep_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [False, True, False, True])

        elif metricName == "Barinel-naive-nf_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [False, False, True, True])
        #--------------------------------
        elif metricName == "Barinel-naive-ef_ep_nf":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [True, True, True, False])
        elif metricName == "Barinel-naive-ef_ep_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [True, True, False, True])
        elif metricName == "Barinel-naive-ef_nf_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [True, False, True, True])
        elif metricName == "Barinel-naive-ep_nf_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [False, True, True, True])
        # --------------------------------
        elif metricName == "Barinel-naive-ef_ep_nf_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [True, True, True, True])