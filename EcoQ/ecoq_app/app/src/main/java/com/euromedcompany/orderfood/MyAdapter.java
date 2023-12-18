package com.euromedcompany.orderfood;
import android.content.Context;
import android.content.Intent;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import com.bumptech.glide.Glide;
import com.makeramen.roundedimageview.RoundedImageView;

import java.util.ArrayList;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

public class MyAdapter extends RecyclerView.Adapter<MyAdapter.MyViewHolder> {

    ArrayList<DataClass> dataList;
    Context context;

    public MyAdapter(ArrayList<DataClass> dataList, Context context) {
        this.dataList = dataList;
        this.context = context;
    }

    @NonNull
    @Override
    public MyViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.staggered_item, parent, false);
        return new MyViewHolder(view);
    }

//        @Override
//    public void onBindViewHolder(@NonNull MyViewHolder holder, int position) {
//        Glide.with(context).load(dataList.get(position).getImageURL()).into(holder.staggeredImages);
//        holder.recyclerTitle.setText(dataList.get(position).getTitle());
//    }

    @Override
    public void onBindViewHolder(@NonNull MyViewHolder holder, int position) {
        Glide.with(context).load(dataList.get(position).getImageURL()).into(holder.staggeredImages);
        holder.recyclerTitle.setText(dataList.get(position).getTitle());

        // Set OnClickListener for the recyclerTitle TextView
        holder.recyclerTitle.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                // Get the selected DataClass item using getAdapterPosition()
                int clickedPosition = holder.getAdapterPosition();
                if (clickedPosition != RecyclerView.NO_POSITION) {
                    DataClass selectedItem = dataList.get(clickedPosition);

                    // Example: Start YourDetailsActivity with the selected item's data
                    Intent intent = new Intent(context, DetailsActivity.class);
                    intent.putExtra("ImageURL", selectedItem.getImageURL());
                    intent.putExtra("Title", selectedItem.getTitle());
                    intent.putExtra("Type", selectedItem.getType());
                    intent.putExtra("Description", selectedItem.getDesc());

                    context.startActivity(intent);
                }
            }
        });
        
    }

    @Override
    public int getItemCount() {
        return dataList.size();
    }

    public class MyViewHolder extends RecyclerView.ViewHolder{

        RoundedImageView staggeredImages;
        TextView recyclerTitle;
        public MyViewHolder(@NonNull View itemView) {
            super(itemView);
            staggeredImages = itemView.findViewById(R.id.staggeredImages);
            recyclerTitle = itemView.findViewById(R.id.recyclerTitle);
        }
    }
}

