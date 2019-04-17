<template>
    <v-container>
        <v-layout column>
            <v-flex>
                <v-btn @click="$refs.upload.click()" block large color="blue-grey" class="white--text" depressed>
                    pick one image to dehaze
                    <v-icon right dark>cloud_upload</v-icon>
                </v-btn>
                <v-btn @click="download" block large color="success" class="white--text" depressed :disabled="!candownload">
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
            candownload: false
        }
    },
    methods: {
        async onImageChanged (e) {
            let files = this.$refs.upload.files;
            if (files.length != 1 || files[0].type.indexOf('image/') === -1) {
                this.bordercolor = 'red'
                this.dialog = true
                this.canclose = true
                this.response.msg = 'FILE TYPE ERROR!'
                return
            }
            let ori_img_tag = this.ori_img;
            //新建一个FileReader对象
            let reader = new FileReader();
            reader.onload = (function (ori_img_tag) {
                return function (e) {
                    //将img标签的src换成base64格式，并显示出来
                    ori_img_tag.src = e.target.result;
                }
            })(ori_img_tag);
            reader.readAsDataURL(files[0])
            ori_img_tag.name = files[0].name
            // 向服务器发送数据
            let formData = new FormData()
            formData.append('file', files[0])
            this.dialog = true
            try {
                const response = await dehazeServiece.dehaze(formData)
                if (response.data.msg === 'ok') {
                    this.bordercolor = 'green'
                    this.response.msg = 'FINISHED!'
                    this.dehaze_img.src = `data:${files[0].type};base64,` + response.data.img
                    this.candownload = true
                }
            } catch(error) {
                this.response.msg = 'NETWORK ERROR!'
                if (error.message.indexOf('timeout') !== -1) {
                    this.response.msg = 'REQEST TIMEOUT!'
                }
                this.bordercolor = 'red'
                
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
