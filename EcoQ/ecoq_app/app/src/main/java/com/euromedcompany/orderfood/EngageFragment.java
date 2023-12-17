package com.euromedcompany.orderfood;

//import android.os.Bundle;
//
//import androidx.fragment.app.Fragment;
//
//import android.view.LayoutInflater;
//import android.view.View;
//import android.view.ViewGroup;
//
//
//public class LiveFragment extends Fragment {
//
//
//    @Override
//    public View onCreateView(LayoutInflater inflater, ViewGroup container,
//                             Bundle savedInstanceState) {
//        // Inflate the layout for this fragment
//        return inflater.inflate(R.layout.fragment_live, container, false);
//    }
//}

//
//import android.content.Intent;
//import android.os.Bundle;
//import android.view.LayoutInflater;
//import android.view.View;
//import android.view.ViewGroup;
//
//import androidx.annotation.NonNull;
//import androidx.fragment.app.Fragment;
//import androidx.recyclerview.widget.LinearLayoutManager;
//import androidx.recyclerview.widget.RecyclerView;
//import androidx.recyclerview.widget.StaggeredGridLayoutManager;
//
//import com.google.android.material.floatingactionbutton.FloatingActionButton;
//import com.google.firebase.database.DataSnapshot;
//import com.google.firebase.database.DatabaseError;
//import com.google.firebase.database.DatabaseReference;
//import com.google.firebase.database.FirebaseDatabase;
//import com.google.firebase.database.ValueEventListener;
//
//import java.util.ArrayList;
//
//public class LiveFragment extends Fragment {
//
//    private RecyclerView recyclerView;
//    private ArrayList<DataClass> dataList;
//    private MyAdapter adapter;
//    private final DatabaseReference databaseReference = FirebaseDatabase.getInstance().getReference("Android Images");
//
//
//    @Override
//    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
//        // Inflate the layout for this fragment
//        View view = inflater.inflate(R.layout.fragment_live, container, false);
//
//       // fab = view.findViewById(R.id.fab);
//        recyclerView = view.findViewById(R.id.recyclerView);
//
//        recyclerView.setHasFixedSize(true);
//        recyclerView.setLayoutManager(new StaggeredGridLayoutManager(2, StaggeredGridLayoutManager.VERTICAL));
//        dataList = new ArrayList<>();
//        adapter = new MyAdapter(dataList, requireContext());
//        recyclerView.setAdapter(adapter);
//
//        databaseReference.addValueEventListener(new ValueEventListener() {
//            @Override
//            public void onDataChange(@NonNull DataSnapshot snapshot) {
//                dataList.clear(); // Clear the list before adding new data
//                for (DataSnapshot dataSnapshot : snapshot.getChildren()) {
//                    DataClass dataClass = dataSnapshot.getValue(DataClass.class);
//                    dataList.add(dataClass);
//                }
//                adapter.notifyDataSetChanged();
//            }
//
//            @Override
//            public void onCancelled(@NonNull DatabaseError error) {
//
//            }
//        });
//
//
//        return view;
//    }
//}




import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.recyclerview.widget.RecyclerView;
import androidx.recyclerview.widget.StaggeredGridLayoutManager;

import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;
import java.util.ArrayList;
public class EngageFragment extends Fragment {
    RecyclerView recyclerView;
    ArrayList<DataClass> dataList;
    MyAdapter adapter;
    final private DatabaseReference databaseReference = FirebaseDatabase.getInstance().getReference("Reports");


    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        // Inflate the layout for this fragment
        View view = inflater.inflate(R.layout.fragment_engage, container, false);


        recyclerView = view.findViewById(R.id.recyclerView);
        recyclerView.setHasFixedSize(true);
        recyclerView.setLayoutManager(new StaggeredGridLayoutManager(2, StaggeredGridLayoutManager.VERTICAL));
        dataList = new ArrayList<>();
        adapter = new MyAdapter(dataList, requireContext());
        recyclerView.setAdapter(adapter);
        databaseReference.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                for (DataSnapshot dataSnapshot : snapshot.getChildren()) {
                    DataClass dataClass = dataSnapshot.getValue(DataClass.class);
                    dataList.add(dataClass);
                }
                adapter.notifyDataSetChanged();
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {
            }
        });
        return view;
    }

}





















