<template>
    <v-container class="main-container">
        <v-layout column>
            <v-flex>
                <v-btn @click="$refs.upload.click()" block large color="blue-grey" class="white--text" depressed>
                    pick one image to dehaze
                    <v-icon right dark>cloud_upload</v-icon>
                </v-btn>
                <v-btn @click="download" block large color="success" class="white--text" depressed :disabled="candownload">
                    download dehazed image
                    <v-icon right dark>cloud_download</v-icon>
                </v-btn>
                <input type="file" id="upload" ref="upload" @change="onImageChanged" accept=".jpg, .jpeg, .png" style="display: none">
                <v-dialog
                v-model="dialog"
                max-width="300"
                max-height="300"
                persistent
                >
                <v-card class="wait-panel">
                    <v-card-title class="headline">dehazing...</v-card-title>
                    <v-progress-circular
                    indeterminate
                    color="primary"
                    v-if="!canclose"
                    >
                    </v-progress-circular>
                    <!-- <Loader></Loader> -->
                    <h3 v-if="canclose">{{response.msg}}</h3>
                    <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn
                        :color=bordercolor
                        flat="flat"
                        @click="dialog = false, canclose = false"
                        v-if="canclose"
                    >
                        close
                    </v-btn>
                    </v-card-actions>
                </v-card>
                </v-dialog>
            </v-flex>
            <v-layout wrap>
                <v-flex xs12 md6>
                    <v-img :src="ori_img.src" transition="slide-y-transition"></v-img>
                </v-flex>
                <v-flex xs12 md6>
                    <v-img :src="dehaze_img.src" transition="slide-y-transition"></v-img>
                </v-flex>
            </v-layout>
        </v-layout>
    </v-container>
</template>

<script>
import dehazeServiece from '@/services/dehazeService'
import Loader from '@/components/Loader'

export default {
    components: {
        Loader
    },
    data () {
        return {
            bordercolor: 'primary',
            response: {
                msg: null
            },
            dialog: false,
            canclose: false,
            ori_img: {
                show: false,
                height: 0,
                width: 0,
                src: '',
                name: null
            },
            dehaze_img: {
                show: false,
                height: 0,
                width: 0,
                src: ''
            },
            candownload: true
        }
    },
    methods: {
        async onImageChanged (e) {
            let _this = this
            // 从input读取文件
            let file = e.target.files[0]
            
            // 创建一个原始图片对象
            let original_image = new Image()

            original_image.onload = function () {
                _this.ori_img.src = original_image.src
                _this.ori_img.width = original_image.naturalWidth
                _this.ori_img.height = original_image.naturalHeight
                _this.dehaze_img.width = original_image.naturalWidth
                _this.dehaze_img.height = original_image.naturalHeight
            }
            //新建一个FileReader对象
            let reader = new FileReader()
            reader.onload = function(e) {
                //将img标签的src换成base64格式，并显示出来
                original_image.src = e.target.result
            }
            await reader.readAsDataURL(file)
            this.ori_img.name = file.name
            this.ori_img.type = file.type
            if (file.type.indexOf('image/') === -1) {
                this.bordercolor = 'red'
                this.dialog = true
                this.canclose = true
                this.response.msg = 'FILE TYPE ERROR!'
                return
            }
            // 向服务器发送数据
            let formData = new FormData()
            formData.append('file', file)
            this.dialog = true
            try {
                const response = await dehazeServiece.dehaze(formData)
                if (response.data.msg === 'ok') {
                    this.bordercolor = 'green'
                    this.response.msg = 'FINISHED!'
                    this.dehaze_img.src = `data:${file.type};base64,` + response.data.img
                    this.candownload = false
                }
            } catch(error) {
                _this.response.msg = 'NETWORK ERROR!'
                if (error.message.indexOf('timeout') !== -1) {
                    _this.response.msg = 'REQEST TIMEOUT!'
                }
                _this.bordercolor = 'red'
                
            } finally {
                this.canclose = true
            }         
        },
        download () {
            let a = document.createElement('a')
            a.href = this.dehaze_img.src
            a.download = `dehaze_${this.ori_img.name}`
            a.click()
        }
    }
  }
</script>

<style scoped>
.wait-panel{
    display: flex;
    flex-direction: column;
    align-items: center;
}
</style>
