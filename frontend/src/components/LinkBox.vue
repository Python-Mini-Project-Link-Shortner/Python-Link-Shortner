<template>
    <div class="card">
        <div class="card-content has-text-left">
            <div class="content">
                <div class="columns">
                    <div class="column is-4 has-text-weight-semibold">Link</div>
                    <div class="column is-8 ellipsis">{{ linkValue.Short_URL }}</div>
                </div>
                <div class="columns">
                    <div class="column is-4 has-text-weight-semibold">Origin</div>
                    <div class="column is-8">
                        <b-tooltip :label="linkValue.Raw_URL" class="is-fullwidth" :position="tooltipPosition">
                            <div class="ellipsis">{{ linkValue.Raw_URL }}</div>
                        </b-tooltip>
                    </div>
                </div>
            </div>
        </div>
        <footer class="card-footer has-background-info">
            <b-button type="is-info" class="card-footer-item"
                v-clipboard="() => linkValue.Short_URL"
                v-clipboard:success="clipboardSuccess"
                v-clipboard:error="clipboardFailer">
                복사
            </b-button>
        </footer>
    </div>
</template>

<script>
export default {
    name: 'LinkBox',
    props: {
        linkValue: {},
        first: false,
        last: false
    },
    computed: {
        tooltipPosition: function() {
            const pos = (this.first === true ? 'right' : (this.last === true ? 'left' : 'top'));
            return 'is-' + pos;
        }
    },
    methods: {
        clipboardSuccess() {
            this.$buefy.snackbar.open('복사되었습니다.');
        },
        clipboardFailer() {
            this.$buefy.snackbar.open('복사에 실패했습니다.');
        }
    }
}
</script>

<style>
    .ellipsis {
        text-overflow: ellipsis;
        white-space: nowrap;
        word-wrap: normal;
        overflow: hidden;
    }

    .is-fullwidth {
        width: 100%;
    }
</style>