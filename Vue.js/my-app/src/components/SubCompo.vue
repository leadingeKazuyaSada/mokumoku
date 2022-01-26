<template>
  <div v-if="flag"><p>Flag = True</p></div>
  <div v-else><p>Flag = False</p></div>
</template>

<script>
export default {
  name: 'SubCompo',
  data () {
    return {
      flag: false
    }
  },
  mounted: function () {
    console.log("mounted hooked.")
    this.flag = true
  }
}
</script>
