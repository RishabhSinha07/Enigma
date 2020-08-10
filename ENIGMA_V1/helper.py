def rotate(l1: list, r) -> list:
    for _ in range(r):
        temp = l1.pop()
        l1.insert(0, temp)
    return l1


def get_rotor(l1: list, l2: list) -> dict:
    setting = {}
    for i in range(len(l1)):
        setting[l1[i]] = l2[i]
    return setting


def rotate_rotor(counter, rotor1_fwd, rotor2_fwd, rotor3_fwd, rotor1_rev,
                 rotor2_rev, rotor3_rev, rt1, rt2, rt3):
    length_rotor1 = len(rotor1_fwd.keys())
    length_rotor2 = len(rotor2_fwd.keys()) + length_rotor1
    length_rotor3 = len(rotor3_fwd.keys()) + length_rotor2

    if counter < length_rotor1:
        # Rotate rotor1_fwd and rotor1_rev by 1 tick
        key11 = list(rotor1_fwd.keys())
        val11 = list(rotor1_fwd.values())
        val11 = rotate(val11, rt1)

        key12 = list(rotor1_rev.keys())
        val12 = list(rotor1_rev.values())
        key12 = rotate(key12, rt1)

        counter += rt1

        rotor1_fwd = get_rotor(key11, val11)
        rotor1_rev = get_rotor(key12, val12)

    elif counter >= length_rotor1 and counter < length_rotor2:

        key21 = list(rotor2_fwd.keys())
        val21 = list(rotor2_fwd.values())
        val21 = rotate(val21, rt2)

        key22 = list(rotor2_rev.keys())
        val22 = list(rotor2_rev.values())
        key22 = rotate(key22, rt2)

        counter += rt2

        rotor2_fwd = get_rotor(key21, val21)
        rotor2_rev = get_rotor(key22, val22)

    else:

        key31 = list(rotor3_fwd.keys())
        val31 = list(rotor3_fwd.values())
        val31 = rotate(val31, rt3)

        key32 = list(rotor3_rev.keys())
        val32 = list(rotor3_rev.values())
        key32 = rotate(key32, rt3)

        counter += rt3

        rotor3_fwd = get_rotor(key31, val31)
        rotor3_rev = get_rotor(key32, val32)

    return counter, rotor1_fwd, rotor2_fwd, rotor3_fwd, rotor1_rev, rotor2_rev, rotor3_rev
