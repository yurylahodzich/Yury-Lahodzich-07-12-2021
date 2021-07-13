<template>
  <v-row align="center" class="list px-3 mx-auto">
    <v-col cols="12" md="8">
      <v-text-field v-model="title" label="Search by Person"></v-text-field>
    </v-col>

    <v-col cols="12" md="4">
      <v-btn small @click="searchMessage">
        Search
      </v-btn>
    </v-col>

    <v-col cols="12" sm="12">
      <v-card class="mx-auto" tile>
        <v-card-title>Received messages</v-card-title>

        <v-data-table
            :headers="headers"
            :items="receivedMessages"
            disable-pagination
            :hide-default-footer="true"
        >
          <template v-slot:[`item.actions`]="{item}">
            <v-icon small @click="deleteMessage(item.id)">mdi-delete</v-icon>
          </template>
        </v-data-table>


      </v-card>
      <v-card class="mx-auto" tile>
        <v-card-title>Sent messages</v-card-title>

        <v-data-table
            :headers="headers"
            :items="sentMessages"
            disable-pagination
            :hide-default-footer="true"
        >
          <template v-slot:[`item.actions`]="{ item }">
            <v-icon small @click="deleteMessage(item.id)">mdi-delete</v-icon>
          </template>
        </v-data-table>

      </v-card>

    </v-col>
  </v-row>
</template>

<script>
import MessageDataService from "../services/MessageDataService";

export default {
  name: "messages-list",
  data() {
    return {
      receivedMessages: [],
      sentMessages: [],
      title: "",
      headers: [
        {text: "Id", align: "start", value: "id"},
        {text: "Subject", sortable: false, value: "subject"},
        {text: "Text", value: "text", sortable: false},
        {text: "Actions", value: "actions", sortable: false},
      ],
    };
  },
  methods: {

    refreshList() {
      this.searchMessage();
    },

    searchMessage() {
      MessageDataService.findById(this.title)
          .then((response) => {
            this.receivedMessages = response.data["received"].map(this.getDisplayMessage)
            this.sentMessages = response.data["sent"].map(this.getDisplayMessage)
          })
          .catch((e) => {
            console.log(e);
          });
    },

    deleteMessage(id) {
      MessageDataService.delete(id)
          .then(() => {
            this.refreshList();
          })
          .catch((e) => {
            console.log(e);
          });
    },

    getDisplayMessage(message) {

      return {
        id: message.id,
        text: message.text.length > 30 ? message.text.substr(0, 30) + "..." : message.text,
        subject: message.subject.length > 30 ? message.subject.substr(0, 30) + "..." : message.subject

      };
    },
  },
  mounted() {

  },
};
</script>

<style>
.list {
  max-width: 750px;
}
</style>
