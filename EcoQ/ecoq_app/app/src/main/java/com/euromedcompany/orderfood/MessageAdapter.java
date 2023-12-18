package com.euromedcompany.orderfood;



import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;
import java.util.Objects;

import me.jagar.chatvoiceplayerlibrary.VoicePlayerView;

public class MessageAdapter extends RecyclerView.Adapter<RecyclerView.ViewHolder> {

    private final ArrayList<MessageModel> messageList;

    public MessageAdapter(ArrayList<MessageModel> messageList) {
        this.messageList = messageList;
    }

    public class UserMessageViewHolder extends RecyclerView.ViewHolder {
        TextView userMsgTV;

        public UserMessageViewHolder(View itemView) {
            super(itemView);
            userMsgTV = itemView.findViewById(R.id.idTVUser);
        }
    }

    public class BotMessageViewHolder extends RecyclerView.ViewHolder {
        TextView botMsgTV;

        public BotMessageViewHolder(View itemView) {
            super(itemView);
            botMsgTV = itemView.findViewById(R.id.idTVBot);
        }
    }

    public class UserAudioViewHolder extends RecyclerView.ViewHolder {
        VoicePlayerView voicePlayerView;

        public UserAudioViewHolder(View itemView) {
            super(itemView);
            voicePlayerView = itemView.findViewById(R.id.voicePlayerView);
        }
    }

    @Override
    public RecyclerView.ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View view;
        if (viewType == 0) {
            view = LayoutInflater.from(parent.getContext())
                    .inflate(R.layout.user_message_item, parent, false);
            return new UserMessageViewHolder(view);
        } else if (viewType == 1) {
            view = LayoutInflater.from(parent.getContext())
                    .inflate(R.layout.bot_message_item, parent, false);
            return new BotMessageViewHolder(view);
        } else {
            view = LayoutInflater.from(parent.getContext())
                    .inflate(R.layout.user_audio_item, parent, false);
            return new UserAudioViewHolder(view);
        }
    }

    @Override
    public void onBindViewHolder(RecyclerView.ViewHolder holder, int position) {
        String sender = messageList.get(position).getSender();
        String type = messageList.get(position).getType();

    //        switch (sender) {
    //            case "user":
    //                ((UserMessageViewHolder) holder).userMsgTV.setText(messageList.get(position).getMessage());
    //                break;
    //            case "bot":
    //                ((BotMessageViewHolder) holder).botMsgTV.setText(messageList.get(position).getMessage());
    //                break;
    //        }
        if (Objects.equals(sender, "user") && Objects.equals(type, "text")) {
            ((UserMessageViewHolder) holder).userMsgTV.setText(messageList.get(position).getMessage());
        } else if (Objects.equals(sender, "bot") && Objects.equals(type, "text")) {
            ((BotMessageViewHolder) holder).botMsgTV.setText(messageList.get(position).getMessage());
        } else if (Objects.equals(sender, "user") && Objects.equals(type, "audio")) {
           ((UserAudioViewHolder) holder).voicePlayerView.setAudio(messageList.get(position).getMessage());
        }
    }

    @Override
    public int getItemCount() {
        return messageList.size();
    }

    @Override
    public int getItemViewType(int position) {
        String sender = messageList.get(position).getSender();
        String type = messageList.get(position).getType();

        if (Objects.equals(sender, "user") && Objects.equals(type, "text")) return 0;
        else if (Objects.equals(sender, "bot") && Objects.equals(type, "text")) return 1;
        else if (Objects.equals(sender, "user") && Objects.equals(type, "audio")) return 2;
        else if (Objects.equals(sender, "bot") && Objects.equals(type, "audio")) return 3;
        else return 4;

        /*
        switch (sender) {
            case "user":
                return 0;
            case "bot":
                return 1;
            default:
                return 1;
        }*/
    }
}
