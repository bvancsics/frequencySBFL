import math

class Algorithm:
    @staticmethod
    def get_act_four_metrics(method, current_four_metrics, w_current_four_metrics, four_bool_vector):
        ef = current_four_metrics[method].ef if four_bool_vector[0] is False else w_current_four_metrics[method].ef
        ep = current_four_metrics[method].ep if four_bool_vector[1] is False else w_current_four_metrics[method].ep
        nf = current_four_metrics[method].nf if four_bool_vector[2] is False else w_current_four_metrics[method].nf
        np = current_four_metrics[method].np if four_bool_vector[3] is False else w_current_four_metrics[method].np
        return ef, ep, nf, np

    @staticmethod
    def get_numerator_weighted_ef(method, w_current_four_metrics):
        return w_current_four_metrics[method].ef

    @staticmethod
    def barinel(ef, ep, w_ef=None):
        tag1 = float(ef) if w_ef is None else float(w_ef)
        tag2 = float(ef) + float(ep)
        if float(tag1) == 0.0 or float(tag2) == 0.0:
            return 0.0
        return float(tag1) / float(tag2)

    @staticmethod
    def dstar(ef, ep, nf, w_ef=None):
        tag1 = float(ef) * float(ef) if w_ef is None else float(w_ef)*float(w_ef)
        tag2 = float(ep) + float(nf)
        if float(tag1) == 0.0:
            return 0.0
        elif float(tag2) == 0.0:
            return float(tag1)
        else:
            return float(tag1) / float(tag2)

    @staticmethod
    def gP13(ef, ep):
        if float(ef) == 0.0:
            return 0.0
        return float(ef)*( 1.0 + 1.0/float( 2.0*float(ep)+float(ef)))

    @staticmethod
    def jaccard(ef, ep, nf, w_ef=None):
        tag1 = float(ef) if w_ef is None else float(w_ef)
        tag2 = float(ef) + float(nf) + float(ep)
        if float(tag1) == 0.0 or float(tag2) == 0.0:
            return 0.0
        else:
            return float(tag1) / float(tag2)

    @staticmethod
    def naish2(ef, ep, np):
        return float(ef)-float(ep)/float(float(ep) + float(np)+1.0)

    @staticmethod
    def ochiai(ef, ep, nf, w_ef=None):
        tag1 = float(ef) if w_ef is None else float(w_ef)
        tag2 = float(float(ef) + float(nf)) * float(float(ef) + float(ep))
        if float(tag1) == 0.0 or float(tag2) == 0.0:
            return 0.0
        return float(tag1) / float(math.sqrt(float(tag2)))

    @staticmethod
    def russel_rao(ef, ep, nf, np, w_ef=None):
        tag1 = float(ef) if w_ef is None else float(w_ef)
        tag2 = float(ef+ep+nf+np)
        if float(tag1) == 0.0 or float(tag2) == 0.0:
            return 0.0
        return float(tag1) / float(tag2)

    @staticmethod
    def sorensen_dice(ef, ep, nf, w_ef=None):
        tag1 = float(ef) * 2.0 if w_ef is None else 2.0*float(w_ef)
        tag2 = 2.0 * float(ef) + float(ep) + float(nf)
        if float(tag1) == 0.0 or float(tag2) == 0.0:
            return 0.0
        return float(tag1) / float(tag2)

    @staticmethod
    def tarantula(ef, ep, nf, np):
        if float(ef + nf) == 0.0:
            return 0.0
        tag1 = float(ef) / float(ef + nf)
        tag2 = float(ef) / float(ef + nf) + float(ep) / float(ep + np)
        if float(tag1) == 0.0 or float(tag2) == 0.0:
            return 0.0
        return float(tag1) / float(tag2)
