/**
 * Created by joey on 2020/04/08.
 */

let nav = new Vue({
  delimiters: ['{', '}'],
  el: '#nav',
  data: {
    activeIndex: undefined
  },
  methods: {
    handleSelect(key, keyPath) {
      this.activeIndex = key;
    }
  }
});