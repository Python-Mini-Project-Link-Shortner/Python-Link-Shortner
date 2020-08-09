<template>
    <div id="ListPage">
        <div class="columns" v-for="n in columnLength" :key="'columns' + n">
            <div class="column" :class="columnClass" v-for="(item, index) in slicedLinkData((n - 1) * columnCount)" :key="item.id">
                <LinkBox :linkValue="item" :first="index === 0" :last="index === columnCount - 1"></LinkBox>
            </div>
        </div>

        <b-pagination
            :total="paginationData.total"
            :current.sync="paginationData.current"
            :range-before="paginationData.rangeBefore"
            :range-after="paginationData.rangeAfter"
            :order="paginationData.order"
            :size="paginationData.size"
            :simple="paginationData.isSimple"
            :rounded="paginationData.isRounded"
            :per-page="paginationData.perPage"
            :icon-prev="paginationData.prevIcon"
            :icon-next="paginationData.nextIcon"
            aria-next-label="Next page"
            aria-previous-label="Previous page"
            aria-page-label="Page"
            aria-current-label="Current page">
        </b-pagination>
    </div>
</template>

<script>
import axios from 'axios'
import LinkBox from '@/components/LinkBox.vue'

// 한 Raw의 최대 Column 갯수
const oneRawColumn = 12;

export default {
    name: 'LinkList',
    components: {
        LinkBox
    },
    data() {
        return {
            linkData: [],
            columnCount: 4,
            paginationData: {
                total: 1, // 총 갯수
                current: 1, // 현재 페이지
                perPage: 12, // 페이지당 아이템 갯수
                rangeBefore: 2, // 현재 페이지 이전에 보여줄 페이지 갯수
                rangeAfter: 2, // 현재 페이지 이후에 보여줄 페이지 갯수
                order: 'is-centered', // 페이지네이션 위치 ('': 좌측정렬, 'is-centered': 가운데, 'is-right': 우측정렬)
                size: '', // 크기 ('is-small', 'default', 'is-medium', 'is-large')
                isSimple: false, // 10개 page 한번에 보여주기
                isRounded: false, // 버튼 동그라미
                prevIcon: 'chevron-left', // 이전페이지 버튼 ('chevron-left', 'arrow-left')
                nextIcon: 'chevron-right' // 다음페이지 버튼 ('chevron-right', 'arrow-right')
            }
        }
    },
    computed: {
        dataPath: function() {
            // Path는 실제 서버에 올라가면 변경되어야 합니다
            return "http://" + window.location.hostname + ":5000/api/test";
        },
        columnClass: function() {
            return 'is-' + parseInt(oneRawColumn / this.columnCount);
        },
        columnLength: function() {
            return Math.ceil(this.linkData.length / this.columnCount);
        }
    },
    methods: {
        getLinkData() {
            // flask에서 자신의 저장된 link들 가져오기
            axios.post(this.dataPath).then((res) => {
                this.linkData = res.data;
            }).catch((error) => {
                console.log(error);
            });
        },
        slicedLinkData(startIdx) {
            return this.linkData.slice(startIdx, startIdx + this.columnCount);
        }
    },  
    created() {
        // 시작시 데이터 초기화
        this.getLinkData();
    }
}
</script>

<style>

</style>