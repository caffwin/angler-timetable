module.exports = {
    z01: (chance) => {
      if (chance < 20) {
        return 'w03'
      } else if (chance < 50) {
        return 'w01'
      } else if (chance < 80) {
        return 'w02'
      } else if (chance < 90) {
        return 'w04'
      } else {
        return 'w05'
      }
    },
    z02: (chance) => {
      if (chance < 20) {
        return 'w03'
      } else if (chance < 50) {
        return 'w01'
      } else if (chance < 70) {
        return 'w02'
      } else if (chance < 80) {
        return 'w09'
      } else if (chance < 90) {
        return 'w04'
      } else {
        return 'w05'
      }
    },
    z03: (chance) => {
      if (chance < 20) {
        return 'w03'
      } else if (chance < 50) {
        return 'w01'
      } else if (chance < 70) {
        return 'w02'
      } else if (chance < 80) {
        return 'w09'
      } else if (chance < 90) {
        return 'w04'
      } else {
        return 'w05'
      }
    },
    z04: (chance) => {
      if (chance < 5) {
        return 'w04'
      } else if (chance < 50) {
        return 'w01'
      } else if (chance < 80) {
        return 'w02'
      } else if (chance < 90) {
        return 'w03'
      } else if (chance < 95) {
        return 'w05'
      } else {
        return 'w06'
      }
    },
    z05: (chance) => {
      if (chance < 10) {
        return 'w04'
      } else if (chance < 40) {
        return 'w01'
      } else if (chance < 60) {
        return 'w02'
      } else if (chance < 80) {
        return 'w03'
      } else if (chance < 90) {
        return 'w09'
      } else {
        return 'w10'
      }
    },
    z06: (chance) => {
      if (chance < 30) {
        return 'w01'
      } else if (chance < 50) {
        return 'w02'
      } else if (chance < 70) {
        return 'w03'
      } else if (chance < 80) {
        return 'w04'
      } else if (chance < 90) {
        return 'w07'
      } else {
        return 'w08'
      }
    },
    z07: (chance) => {
      if (chance < 30) {
        return 'w01'
      } else if (chance < 50) {
        return 'w02'
      } else if (chance < 70) {
        return 'w03'
      } else if (chance < 85) {
        return 'w04'
      } else {
        return 'w05'
      }
    },
    z08: (chance) => {
      if (chance < 20) {
        return 'w03'
      } else if (chance < 50) {
        return 'w01'
      } else if (chance < 80) {
        return 'w02'
      } else if (chance < 90) {
        return 'w04'
      } else {
        return 'w05'
      }
    },
    z32: (chance) => {
      if (chance < 20) {
        return 'w03'
      } else if (chance < 50) {
        return 'w01'
      } else if (chance < 80) {
        return 'w02'
      } else if (chance < 90) {
        return 'w04'
      } else {
        return 'w08'
      }
    },
    z09: (chance) => {
      if (chance < 20) {
        return 'w05'
      } else if (chance < 30) {
        return 'w04'
      } else if (chance < 40) {
        return 'w03'
      } else if (chance < 55) {
        return 'w02'
      } else if (chance < 85) {
        return 'w01'
      } else {
        return 'w02'
      }
    },
    z10: (chance) => {
      if (chance < 5) {
        return 'w07'
      } else if (chance < 20) {
        return 'w05'
      } else if (chance < 30) {
        return 'w04'
      } else if (chance < 40) {
        return 'w03'
      } else if (chance < 55) {
        return 'w02'
      } else if (chance < 85) {
        return 'w01'
      } else {
        return 'w02'
      }
    },
    z11: (chance) => {
      if (chance < 5) {
        return 'w07'
      } else if (chance < 20) {
        return 'w05'
      } else if (chance < 30) {
        return 'w04'
      } else if (chance < 40) {
        return 'w03'
      } else if (chance < 55) {
        return 'w02'
      } else if (chance < 85) {
        return 'w01'
      } else {
        return 'w02'
      }
    },
    z12: (chance) => {
      if (chance < 5) {
        return 'w04'
      } else if (chance < 10) {
        return 'w08'
      } else if (chance < 25) {
        return 'w07'
      } else if (chance < 30) {
        return 'w04'
      } else if (chance < 40) {
        return 'w03'
      } else if (chance < 70) {
        return 'w02'
      } else {
        return 'w01'
      }
    },
    z13: (chance) => {
      if (chance < 5) {
        return 'w04'
      } else if (chance < 10) {
        return 'w06'
      } else if (chance < 25) {
        return 'w05'
      } else if (chance < 30) {
        return 'w04'
      } else if (chance < 40) {
        return 'w03'
      } else if (chance < 70) {
        return 'w02'
      } else {
        return 'w01'
      }
    },
    z14: (chance) => {
      if (chance < 5) {
        return 'w03'
      } else if (chance < 20) {
        return 'w05'
      } else if (chance < 30) {
        return 'w04'
      } else if (chance < 40) {
        return 'w03'
      } else if (chance < 55) {
        return 'w02'
      } else if (chance < 85) {
        return 'w01'
      } else {
        return 'w02'
      }
    },
    z15: (chance) => {
      if (chance < 40) {
        return 'w01'
      } else if (chance < 60) {
        return 'w02'
      } else if (chance < 85) {
        return 'w03'
      } else if (chance < 95) {
        return 'w04'
      } else {
        return 'w05'
      }
    },
    z16: (chance) => {
      if (chance < 40) {
        return 'w01'
      } else if (chance < 60) {
        return 'w02'
      } else if (chance < 85) {
        return 'w03'
      } else if (chance < 95) {
        return 'w04'
      } else {
        return 'w05'
      }
    },
    z17: (chance) => {
      if (chance < 15) {
        return 'w14'
      } else if (chance < 55) {
        return 'w01'
      } else if (chance < 75) {
        return 'w02'
      } else if (chance < 85) {
        return 'w03'
      } else if (chance < 95) {
        return 'w04'
      } else {
        return 'w05'
      }
    },
    z18: (chance) => {
      if (chance < 40) {
        return 'w01'
      } else if (chance < 60) {
        return 'w02'
      } else if (chance < 70) {
        return 'w03'
      } else if (chance < 80) {
        return 'w04'
      } else if (chance < 85) {
        return 'w05'
      } else {
        return 'w06'
      }
    },
    z19: (chance) => {
      if (chance < 20) {
        return 'w13'
      } else if (chance < 60) {
        return 'w01'
      } else if (chance < 80) {
        return 'w02'
      } else if (chance < 90) {
        return 'w03'
      } else {
        return 'w04'
      }
    },
    z20: (chance) => {
      if (chance < 5) {
        return 'w01'
      } else if (chance < 20) {
        return 'w02'
      } else if (chance < 50) {
        return 'w03'
      } else {
        return 'w04'
      }
    },
    z21: (chance) => {
      if (chance < 40) {
        return 'w01'
      } else if (chance < 60) {
        return 'w02'
      } else if (chance < 85) {
        return 'w03'
      } else if (chance < 95) {
        return 'w04'
      } else {
        return 'w05'
      }
    },
    z22: (chance) => {
      if (chance < 15) {
        return 'w03'
      } else if (chance < 30) {
        return 'w04'
      } else if (chance < 60) {
        return 'w16'
      } else if (chance < 75) {
        return 'w01'
      } else {
        return 'w02'
      }
    },
    z23: (chance) => {
      if (chance < 60) {
        return 'w11'
      } else if (chance < 70) {
        return 'w02'
      } else if (chance < 75) {
        return 'w01'
      } else if (chance < 90) {
        return 'w03'
      } else {
        return 'w04'
      }
    },
    z24: (chance) => {
      if (chance < 20) {
        return 'w12'
      } else if (chance < 60) {
        return 'w11'
      } else if (chance < 70) {
        return 'w02'
      } else if (chance < 75) {
        return 'w01'
      } else if (chance < 90) {
        return 'w03'
      } else {
        return 'w04'
      }
    },
    z25: (chance) => {
      if (chance < 20) {
        return 'w12'
      } else if (chance < 60) {
        return 'w11'
      } else if (chance < 70) {
        return 'w02'
      } else if (chance < 75) {
        return 'w01'
      } else if (chance < 90) {
        return 'w03'
      } else {
        return 'w04'
      }
    },
    z26: (chance) => {
      if (chance < 30) {
        return 'w01'
      } else if (chance < 60) {
        return 'w02'
      } else if (chance < 70) {
        return 'w03'
      } else if (chance < 80) {
        return 'w04'
      } else if (chance < 90) {
        return 'w09'
      } else {
        return 'w18'
      }
    },
    z27: (chance) => {
      if (chance < 35) {
        return 'w02'
      } else if (chance < 70) {
        return 'w03'
      } else {
        return 'w07'
      }
    },
    z28: (chance) => {
      if (chance < 10) {
        return 'w03'
      } else if (chance < 20) {
        return 'w04'
      } else if (chance < 30) {
        return 'w07'
      } else if (chance < 40) {
        return 'w14'
      } else if (chance < 70) {
        return 'w01'
      } else {
        return 'w02'
      }
    },
    z29: (chance) => {
      if (chance < 10) {
        return 'w03'
      } else if (chance < 20) {
        return 'w04'
      } else if (chance < 30) {
        return 'w05'
      } else if (chance < 40) {
        return 'w06'
      } else if (chance < 70) {
        return 'w01'
      } else {
        return 'w02'
      }
    },
    z30: (chance) => {
      if (chance < 10) {
        return 'w03'
      } else if (chance < 20) {
        return 'w10'
      } else if (chance < 40) {
        return 'w17'
      } else if (chance < 70) {
        return 'w01'
      } else {
        return 'w02'
      }
    },
    z31: (chance) => {
      if (chance < 10) {
        return 'w03'
      } else if (chance < 20) {
        return 'w04'
      } else if (chance < 30) {
        return 'w05'
      } else if (chance < 40) {
        return 'w06'
      } else if (chance < 70) {
        return 'w01'
      } else {
        return 'w02'
      }
    },
    z33: (chance) => {
      if ((chance -= 15) < 0) {
        return 'w01'
      } else if ((chance -= 45) < 0) {
        return 'w02'
      } else if ((chance -= 20) < 0) {
        return 'w03'
      } else if ((chance -= 10) < 0) {
        return 'w04'
      } else {
        return 'w07'
      }
    },
    z34: (chance) => {
      if ((chance -= 15) < 0) {
        return 'w01'
      } else if ((chance -= 45) < 0) {
        return 'w02'
      } else if ((chance -= 20) < 0) {
        return 'w03'
      } else if ((chance -= 10) < 0) {
        return 'w04'
      } else {
        return 'w07'
      }
    },
    z35: (chance) => {
      if ((chance -= 10) < 0) {
        return 'w01'
      } else if ((chance -= 50) < 0) {
        return 'w02'
      } else if ((chance -= 15) < 0) {
        return 'w03'
      } else if ((chance -= 10) < 0) {
        return 'w04'
      } else if ((chance -= 10) < 0) {
        return 'w09'
      } else {
        return 'w14'
      }
    },
    z36: (chance) => {
      if ((chance -= 20) < 0) {
        return 'w01'
      } else if ((chance -= 40) < 0) {
        return 'w02'
      } else if ((chance -= 20) < 0) {
        return 'w03'
      } else if ((chance -= 10) < 0) {
        return 'w04'
      } else {
        return 'w08'
      }
    },
    z37: (chance) => {
      if ((chance -= 10) < 0) {
        return 'w05'
      } else if ((chance -= 10) < 0) {
        return 'w04'
      } else if ((chance -= 20) < 0) {
        return 'w03'
      } else if ((chance -= 40) < 0) {
        return 'w02'
      } else {
        return 'w01'
      }
    },
    z38: (chance) => {
      if ((chance -= 10) < 0) {
        return 'w05'
      } else if ((chance -= 10) < 0) {
        return 'w04'
      } else if ((chance -= 20) < 0) {
        return 'w03'
      } else if ((chance -= 40) < 0) {
        return 'w02'
      } else {
        return 'w01'
      }
    },
    z39: (chance) => {
      if ((chance -= 10) < 0) {
        return 'w07'
      } else if ((chance -= 10) < 0) {
        return 'w09'
      } else if ((chance -= 15) < 0) {
        return 'w03'
      } else if ((chance -= 40) < 0) {
        return 'w02'
      } else {
        return 'w01'
      }
    },
    z40: (chance) => {
      if ((chance -= 5) < 0) {
        return 'w06'
      } else if ((chance -= 10) < 0) {
        return 'w05'
      } else if ((chance -= 10) < 0) {
        return 'w04'
      } else if ((chance -= 15) < 0) {
        return 'w03'
      } else if ((chance -= 40) < 0) {
        return 'w02'
      } else {
        return 'w01'
      }
    },
    z41: (chance) => {
      if ((chance -= 5) < 0) {
        return 'w10'
      } else if ((chance -= 5) < 0) {
        return 'w09'
      } else if ((chance -= 7) < 0) {
        return 'w05'
      } else if ((chance -= 8) < 0) {
        return 'w04'
      } else if ((chance -= 10) < 0) {
        return 'w03'
      } else if ((chance -= 40) < 0) {
        return 'w02'
      } else {
        return 'w01'
      }
    }
  }