<template>
  <div>
    <v-row align="center" class="list px-3 mx-auto">
      <v-col cols="12" md="12">
        <v-text-field v-model="id" name="id"  type="number" label="Search by Person" @input="findById(id) "></v-text-field>
      </v-col>

      <v-col cols="12" sm="12">
        <v-card class="mx-auto" tile>
          <v-card-title>Received messages</v-card-title>

          <v-data-table
              :headers="headers"
              :items="receivedList"
              disable-pagination
              :hide-default-footer="true"
          >
            <template v-slot:[`item.actions`]="{item}">
              <v-icon small @click="dialog = true; currentItem = item;">mdi-delete</v-icon>
            </template>
          </v-data-table>


        </v-card>
        <v-card class="mx-auto" tile>
          <v-card-title>Sent messages</v-card-title>

          <v-data-table
              :headers="headers"
              :items="sentList"
              disable-pagination
              :hide-default-footer="true"
          >
            <template v-slot:[`item.actions`]="{item}">
              <v-icon small @click="dialog = true; currentItem = item;">mdi-delete</v-icon>
            </template>
          </v-data-table>

        </v-card>

      </v-col>
    </v-row>

    <v-dialog
      v-model="dialog"
      width="500"
    >
      <v-card>
        <v-card-title class="text-h5 grey lighten-2">
          Attention
        </v-card-title>

        <v-card-text>
         Message will be deleted
        </v-card-text>



        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="localDeleteMessage(currentItem.id)"
          >
            I accept
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>

import {
  mapGetters,
  mapActions
} from "vuex";

export default {
  name: 'MessagesList',
  data() {
    return {
      id: null,
      dialog: false,
      headers: [
        {text: "Id", align: "start", value: "id"},
        {text: "Subject", sortable: false, value: "subject"},
        {text: "Text", value: "text", sortable: false},
        {text: "Actions", value: "actions", sortable: false},
      ],
      currentItem: null
    }
  },
  methods: {
    ...mapActions(["findById","deleteMessage"]),
    localDeleteMessage (itemId) {
      this.deleteMessage(itemId)
      this.dialog = false
    }
  },
  computed: mapGetters(["sentList", "receivedList"]),
}
</script>

<style>
.list {
  max-width: 750px;
}
</style>
