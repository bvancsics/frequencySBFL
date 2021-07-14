import algorithms


# four_bool_vector=[ef, ep, nf, np])

class Tarantula(algorithms.Algorithm):
    def init_score(self, methodNames):
        self.score = {}
        for m in methodNames:
            self.score[m] = 0.0

    def calculation(self, methodNames, current_four_metrics=None, w_current_four_metrics=None, four_bool_vector=None):
        for method in methodNames:
            ef, ep, nf, np = self.get_act_four_metrics(method, current_four_metrics, w_current_four_metrics, four_bool_vector)
            self.score[method] = self.tarantula(ef, ep, nf, np)
        return self.score


    def call(self, metricName, methodNames, hit_results, unique_results, naive_results):
        self.init_score(methodNames)
        if metricName == "Tarantula-hit":
            return self.calculation(methodNames,
                                    hit_results,
                                    None,
                                    [False, False, False, False])
        elif metricName == "Tarantula-unique-ef":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [True, False, False, False])
        elif metricName == "Tarantula-unique-ep":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [False, True, False, False])
        elif metricName == "Tarantula-unique-nf":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [False, False, True, False])
        elif metricName == "Tarantula-unique-np":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [False, False, False, True])
        # --------------------------------
        elif metricName == "Tarantula-unique-ef_ep":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [True, True, False, False])
        elif metricName == "Tarantula-unique-ef_nf":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [True, False, True, False])
        elif metricName == "Tarantula-unique-ef_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [True, False, False, True])
        elif metricName == "Tarantula-unique-ep_nf":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [False, True, True, False])
        elif metricName == "Tarantula-unique-ep_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [False, True, False, True])
        elif metricName == "Tarantula-unique-nf_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [False, False, True, True])
        #--------------------------------
        elif metricName == "Tarantula-unique-ef_ep_nf":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [True, True, True, False])
        elif metricName == "Tarantula-unique-ef_ep_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [True, True, False, True])
        elif metricName == "Tarantula-unique-ef_nf_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [True, False, True, True])
        elif metricName == "Tarantula-unique-ep_nf_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [False, True, True, True])
        # --------------------------------
        elif metricName == "Tarantula-unique-ef_ep_nf_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    unique_results,
                                    [True, True, True, True])
        # ============================================================
        # ============================================================
        elif metricName == "Tarantula-naive-ef":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [True, False, False, False])
        elif metricName == "Tarantula-naive-ep":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [False, True, False, False])
        elif metricName == "Tarantula-naive-nf":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [False, False, True, False])
        elif metricName == "Tarantula-naive-np":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [False, False, False, True])
        # --------------------------------
        elif metricName == "Tarantula-naive-ef_ep":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [True, True, False, False])
        elif metricName == "Tarantula-naive-ef_nf":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [True, False, True, False])
        elif metricName == "Tarantula-naive-ef_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [True, False, False, True])
        elif metricName == "Tarantula-naive-ep_nf":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [False, True, True, False])
        elif metricName == "Tarantula-naive-ep_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [False, True, False, True])

        elif metricName == "Tarantula-naive-nf_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [False, False, True, True])
        #--------------------------------
        elif metricName == "Tarantula-naive-ef_ep_nf":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [True, True, True, False])
        elif metricName == "Tarantula-naive-ef_ep_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [True, True, False, True])
        elif metricName == "Tarantula-naive-ef_nf_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [True, False, True, True])
        elif metricName == "Tarantula-naive-ep_nf_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [False, True, True, True])
        # --------------------------------
        elif metricName == "Tarantula-naive-ef_ep_nf_np":
            return self.calculation(methodNames,
                                    hit_results,
                                    naive_results,
                                    [True, True, True, True])
