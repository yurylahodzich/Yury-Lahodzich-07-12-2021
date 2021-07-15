<template>
  <div class="submit-form mt-3 mx-auto">
    <p class="headline">Send message</p>

    <div>
      <v-form ref="form" lazy-validation>
        <v-text-field
            v-model="newMessageForm.sender_id"
            label="Sender"
            type="number"
            required
        ></v-text-field>
        <v-text-field
            v-model="newMessageForm.receiver_id"
            label="Receiver"
            type="number"
            required
        ></v-text-field>
        <v-text-field
            v-model="newMessageForm.text"
            label="Text"
            required
        ></v-text-field>
        <v-text-field
            v-model="newMessageForm.subject"
            label="Subject"
            required
        ></v-text-field>
      </v-form>

      <v-btn :disabled="!isComplete" color="primary" class="mt-3" @click="addMessage(newMessageForm)">Submit</v-btn>

    </div>
  </div>
</template>

<script>
import {
  mapActions, mapGetters
} from "vuex";

export default {
  name: "add-message",
  data: () => ({
    isFormValid: false,
  }),

  methods: {
    ...mapActions(["addMessage"]),
  },
  computed: mapGetters(["newMessageForm","isComplete"]),

};
</script>

<style>
.submit-form {
  max-width: 300px;
}
</style>
