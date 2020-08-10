import json
import helper as helper


def crypto(rotor1_fwd, rotor2_fwd, rotor3_fwd, rotor1_rev, rotor2_rev,
           rotor3_rev, reflector, rt1, rt2, rt3):
    counter = 0
    input_st = input(
        "INPUT STRING ONLY ALPHABETS NO SPECIAL CHARACTERS OR NUMBERS: "
    ).lower()
    coded_string = ""
    for i in range(len(input_st)):
        if input_st[i] == " ":
            coded_string += " "
        else:
            val = rotor1_rev[rotor2_rev[rotor3_rev[reflector[rotor3_fwd[
                rotor2_fwd[rotor1_fwd[input_st[i]]]]]]]]
            coded_string += val
        counter, rotor1_fwd, rotor2_fwd, rotor3_fwd, rotor1_rev, rotor2_rev, rotor3_rev = helper.rotate_rotor(
            counter, rotor1_fwd, rotor2_fwd, rotor3_fwd, rotor1_rev,
            rotor2_rev, rotor3_rev, rt1, rt2, rt3)

    print(coded_string)


if __name__ == "__main__":

    # Importing the settings for machine

    f1 = open('ENIGMA_V1\config.json')
    config = json.load(f1)
    f1.close()

    # Create Rotor every step
    rotor1_fwd = helper.get_rotor(config["rotor1"]["left"],
                                  config["rotor1"]["right"])
    rotor2_fwd = helper.get_rotor(config["rotor2"]["left"],
                                  config["rotor2"]["right"])
    rotor3_fwd = helper.get_rotor(config["rotor3"]["left"],
                                  config["rotor3"]["right"])

    rotor1_rev = helper.get_rotor(config["rotor1"]["right"],
                                  config["rotor1"]["left"])
    rotor2_rev = helper.get_rotor(config["rotor2"]["right"],
                                  config["rotor2"]["left"])
    rotor3_rev = helper.get_rotor(config["rotor3"]["right"],
                                  config["rotor3"]["left"])

    reflector = config["reflector"]

    rt1 = config["rotation_tick_rotor1"]
    rt2 = config["rotation_tick_rotor2"]
    rt3 = config["rotation_tick_rotor3"]

    crypto(rotor1_fwd, rotor2_fwd, rotor3_fwd, rotor1_rev, rotor2_rev,
           rotor3_rev, reflector, rt1, rt2, rt3)