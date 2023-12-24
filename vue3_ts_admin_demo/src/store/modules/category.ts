import { defineStore } from 'pinia'
import { CategoryState } from './types/type'
import { CategoryResponseData } from '@/api/product/attr/type'
import { reqC1, reqC2, reqC3 } from '@/api/product/attr'

const useCategoryStore = defineStore('Category', {
  state: (): CategoryState => {
    return {
      //存储一级分类的数据
      c1Arr: [],
      //存储一级分类的ID
      c1Id: '',
      //存储对应一级分类下二级分类的数据
      c2Arr: [],
      //收集二级分类的ID
      c2Id: '',
      //存储三级分类的数据
      c3Arr: [],
      //存储三级分类的ID
      c3Id: '',
    }
  },
  actions: {
    async getC1() {
      const result: CategoryResponseData = await reqC1()
      if (result.code == 200) {
        this.c1Arr = result.data
      }
    },
    //获取二级分类的数据
    async getC2() {
      //获取对应一级分类的下二级分类的数据
      const result: CategoryResponseData = await reqC2(this.c1Id)
      if (result.code == 200) {
        this.c2Arr = result.data
      }
    },
    //获取三级分类的数据
    async getC3() {
      const result: CategoryResponseData = await reqC3(this.c2Id)
      if (result.code == 200) {
        this.c3Arr = result.data
      }
    },
  },
  getters: {},
})

export default useCategoryStore
