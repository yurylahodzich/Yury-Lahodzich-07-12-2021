import MessageDataService from "../../services/MessageDataService";

const state = {
    receivedMessages: [],
    sentMessages: [],
    newMessageForm: {
        sender_id: null,
        receiver_id: null,
        text: "",
        subject: "",
    }
};

const getters = {
    receivedList: state => state.receivedMessages,
    sentList: state => state.sentMessages,
    newMessageForm: state => state.newMessageForm,
    isComplete(){
    return state.newMessageForm.receiver_id && state.newMessageForm.sender_id;
  },
};

const actions = {
    async addMessage({commit}, message) {
        await MessageDataService.create(message)
        commit("clearMessageInput")
    },
    async findById({commit}, id) {
        if (id) {
            const response = await MessageDataService.findById(id)
            commit("setMessages", response.data)
        }

    },
    async deleteMessage({commit}, id) {
        await MessageDataService.delete(id)
        commit("removeMessage", id)
    }
};

const mutations = {
    removeMessage: (state, id) => (
        state.receivedMessages = state.receivedMessages.filter(message => message.id !== id),
            state.sentMessages = state.sentMessages.filter(message => message.id !== id)

    ),
    setMessages: (state, messages) =>
        (
            state.receivedMessages = messages.received, state.sentMessages = messages.sent
        ),
    clearMessageInput:(state)=>(
        state.newMessageForm={
        sender_id: null,
        receiver_id: null,
        text: "",
        subject: "",
    }
)
};

export default {
    state,
    getters,
    actions,
    mutations
}