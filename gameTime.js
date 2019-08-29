import Vue from 'vue'
import Vuex from 'vuex'
import _ from 'lodash'
Vue.use(Vuex)

const getWeatherSeed = (time, shift) => {
  // Thanks to Rogueadyn's SaintCoinach library for this calculation.
  // lDate is the current local time.

  let unixSeconds = parseInt(time / 1000) + shift * 1400
  // Get Eorzea hour for weather start
  let bell = unixSeconds / 175

  // Do the magic 'cause for calculations 16:00 is 0, 00:00 is 8 and 08:00 is 16
  let increment = (bell + 8 - (bell % 8)) % 24

  // Take Eorzea days since unix epoch
  let totalDays = unixSeconds / 4200
  totalDays = (totalDays << 32) >>> 0 // Convert to uint

  // 0x64 = 100
  let calcBase = totalDays * 100 + increment

  // 0xB = 11
  let step1 = ((calcBase << 11) ^ calcBase) >>> 0
  let step2 = ((step1 >>> 8) ^ step1) >>> 0

  // 0x64 = 100
  return step2 % 100
}

const getForecastSeed = (time, shift) => {
  // Thanks to Rogueadyn's SaintCoinach library for this calculation.
  // lDate is the current local time.

  let unixSeconds = parseInt(time / 1000) + shift * 1400
  // Get Eorzea hour for weather start
  let bell = unixSeconds / 175

  // Do the magic 'cause for calculations 16:00 is 0, 00:00 is 8 and 08:00 is 16
  let increment = (bell + 8 - (bell % 8)) % 24

  console.log((bell - (bell % 8)) % 24)

  // Take Eorzea days since unix epoch
  let totalDays = unixSeconds / 4200
  totalDays = (totalDays << 32) >>> 0 // Convert to uint

  // 0x64 = 100
  let calcBase = totalDays * 100 + increment

  // 0xB = 11
  let step1 = ((calcBase << 11) ^ calcBase) >>> 0
  let step2 = ((step1 >>> 8) ^ step1) >>> 0

  // 0x64 = 100
  return {
    bell: (bell - (bell % 8)) % 24,
    seed: step2 % 100
  }
}

const state = {
  time: 0, // Unix Milliseconds
  weatherStart: 0,
  weatherSeeds: [],
  forecastSeeds: []
}

const actions = {
  watchTime ({commit}) {
    const range = _.range(-1, 6)

    setInterval(() => {
      let time = new Date().getTime()
      commit('SET_TIME', time)

      let start = parseInt(time / 1000 / 1400)
      if (state.weatherStart === start) return

      commit('SET_WEATHER_START', start)

      let weatherSeeds = range.map((shift) => {
        return getWeatherSeed(time, shift)
      })
      commit('SET_WEATHER_SEEDS', weatherSeeds)

      let weatherForecasts = range.map((shift) => {
        return getForecastSeed(time, shift)
      })
      commit('SET_FORECAST_SEEDS', weatherForecasts)
    }, 100)
  }
}

const mutations = {
  SET_TIME (state, time) {
    state.time = time
  },
  SET_WEATHER_START (state, start) {
    state.weatherStart = start
  },
  SET_WEATHER_SEEDS (state, seeds) {
    state.weatherSeeds = seeds
  },
  SET_FORECAST_SEEDS (state, seeds) {
    state.forecastSeeds = seeds
  }
}

const getters = {
  weatherStartTime: (state) => (shift) => {
    let time = (state.weatherStart + shift) % 3 * 8
    return ('0' + String(time)).slice(-2) + ':00'
  },
  eoTime: (state) => {
    let bell = parseInt(state.time / 1000 / 175) % 24
    let min = parseInt(state.time / 1000 / 35 * 12) % 60
    return ('0' + String(bell)).slice(-2) + ':' + ('0' + String(min)).slice(-2)
  }
}

export default new Vuex.Store({
  state,
  actions,
  mutations,
  getters
})
