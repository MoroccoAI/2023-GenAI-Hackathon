package com.euromedcompany.orderfood;
// YourDetailsActivity.java

import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.bumptech.glide.Glide;

public class DetailsActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_details);

        // Retrieve data from the Intent
        String imageURL = getIntent().getStringExtra("ImageURL");
        String title = getIntent().getStringExtra("Title");
        String type = getIntent().getStringExtra("Type");
        String description = getIntent().getStringExtra("Description");

        // Display details in your activity's views
        ImageView imageView = findViewById(R.id.ImageView);
        TextView titleTextView = findViewById(R.id.TitleTextView);
        TextView typeTextView =  findViewById(R.id.TypeTextView);
        TextView DescriptionTextView =  findViewById(R.id.DescriptionTextView);
        // Load image using Glide or your preferred image loading library
        Glide.with(this).load(imageURL).into(imageView);

        // Set the title text
        titleTextView.setText(title);
        typeTextView.setText(type);
        DescriptionTextView.setText(description);
    }
}

