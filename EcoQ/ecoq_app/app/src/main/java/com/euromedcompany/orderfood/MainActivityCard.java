package com.euromedcompany.orderfood;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentManager;
import androidx.fragment.app.FragmentTransaction;

import com.euromedcompany.orderfood.databinding.ActivityMainCardBinding;

public class MainActivityCard extends AppCompatActivity {
    ActivityMainCardBinding binding;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding = ActivityMainCardBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());
        replaceFragment(new HomeFragment());
        binding.bottomNavigationView.setBackground(null);
        binding.bottomNavigationView.setOnItemSelectedListener(item -> {
            int itemId = item.getItemId();
            if (itemId == R.id.home) {
                replaceFragment(new HomeFragment());

            } else if (itemId == R.id.report) {
                replaceFragment(new ReportFragment());

            } else if (itemId == R.id.ecoChat) {


                //replaceFragment(new EcoChatFragment());
                startActivity(new Intent(this, EcoChatActivity.class));



            } else if (itemId == R.id.engage) {

                replaceFragment(new EngageFragment());
            } else if (itemId == R.id.explore) {
                replaceFragment(new ExploreFragment());

            }
            return true;
        });


    }
    private void replaceFragment(Fragment fragment) {
        FragmentManager fragmentManager = getSupportFragmentManager();
        FragmentTransaction fragmentTransaction = fragmentManager.beginTransaction();
        fragmentTransaction.replace(R.id.frame_layout, fragment);
        fragmentTransaction.commit();
    }


}