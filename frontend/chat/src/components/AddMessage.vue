<template>
  <div class="submit-form mt-3 mx-auto">
    <p class="headline">Send message</p>

    <div v-if="!submitted">
      <v-form ref="form" lazy-validation>
        <v-text-field
            v-model="message.sender"
            :rules="[(v) => !!v || 'Sender is required']"
            label="Sender"
            type="number"
            required
        ></v-text-field>
        <v-text-field
            v-model="message.receiver"
            :rules="[(v) => !!v || 'Receiver is required']"
            label="Receiver"
            required
        ></v-text-field>
        <v-text-field
            v-model="message.text"
            :rules="[(v) => !!v || 'Title is required']"
            label="Text"
            required
        ></v-text-field>
        <v-text-field
            v-model="message.subject"
            :rules="[(v) => !!v || 'Subject is required']"
            label="Subject"
            required
        ></v-text-field>
      </v-form>

      <v-btn color="primary" class="mt-3" @click="saveMessage">Submit</v-btn>
    </div>

    <div v-else>
      <v-card class="mx-auto">
        <v-card-title>
          Submitted successfully!
        </v-card-title>

        <v-card-subtitle>
          Click the button to add new Message.
        </v-card-subtitle>

        <v-card-actions>
          <v-btn color="success" @click="newMessage">Add</v-btn>
        </v-card-actions>
      </v-card>
    </div>
  </div>
</template>

<script>
import MessageDataService from "../services/MessageDataService";

export default {
  name: "add-message",
  data() {
    return {
      message: {
        id: null,
        sender: null,
        receiver: null,
        text: "",
        subject:"",
      },
      submitted: false,
    };
  },
  methods: {
    saveMessage() {
      var data = {
        sender_id: this.message.sender,
        receiver_id: this.message.receiver,
        text: this.message.text,
        subject:this.message.subject,
      };

      MessageDataService.create(data)
          .then((response) => {
            this.message.id = response.data.id;
            console.log(response.data);
            this.submitted = true;
          })
          .catch((e) => {
            console.log(e);
          });
    },

    newMessage() {
      this.submitted = false;
      this.message = {};
    },
  },
};
</script>

<style>
.submit-form {
  max-width: 300px;
}
</style>
