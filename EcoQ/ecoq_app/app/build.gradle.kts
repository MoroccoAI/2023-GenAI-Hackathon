plugins {
    id("com.android.application")
    id("com.google.gms.google-services")
}

android {
    namespace = "com.euromedcompany.orderfood"
    compileSdk = 34

    defaultConfig {
        applicationId = "com.euromedcompany.orderfood"
        minSdk = 24
        targetSdk = 33
        versionCode = 1
        versionName = "1.0"

        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"
    }

    buildTypes {
        release {
            isMinifyEnabled = false
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_1_8
        targetCompatibility = JavaVersion.VERSION_1_8
    }

    buildFeatures {
        viewBinding = true
        dataBinding = true
    }
}

dependencies {
    implementation("com.google.android.material:material:1.3.0-alpha02")
    implementation("androidx.core:core-ktx:1.12.0")
    implementation("com.android.volley:volley:1.2.1")
    implementation("com.github.JagarYousef:ChatVoicePlayer:1.1.0")
    implementation("com.github.3llomi:RecordView:3.1.3")
    //noinspection GradleCompatible
    implementation ("androidx.appcompat:appcompat:1.1.0")
    //implementation("androidx.appcompat:appcompat:1.6.1")
    implementation("com.google.android.material:material:1.10.0")
    implementation("androidx.constraintlayout:constraintlayout:2.1.4")
    implementation(platform("com.google.firebase:firebase-bom:32.6.0"))
    implementation("com.google.firebase:firebase-auth:22.3.0")
    implementation("com.google.firebase:firebase-storage:20.3.0")
    implementation("androidx.core:core:1.12.0")
    implementation("androidx.databinding:databinding-runtime:8.2.0")
    // implementation(project(mapOf("path" to ":app")))
    testImplementation("junit:junit:4.13.2")
    androidTestImplementation("androidx.test.ext:junit:1.1.5")
    androidTestImplementation("androidx.test.espresso:espresso-core:3.5.1")

    // Library
    implementation ("com.google.firebase:firebase-core:10.2.0")
    implementation ("com.google.firebase:firebase-database:10.2.0")
    implementation ("info.hoang8f:fbutton:1.0.5")

    implementation ("com.rengwuxian.materialedittext:library:2.1.4")

    implementation("com.airbnb.android:lottie:3.4.1")

    implementation("com.github.bumptech.glide:glide:4.14.2")
    annotationProcessor("com.github.bumptech.glide:compiler:4.14.2")
    implementation("com.makeramen:roundedimageview:2.3.0")

    implementation("com.github.JagarYousef:ChatVoicePlayer:1.1.0")
    implementation("com.github.3llomi:RecordView:3.1.3")



    // wav
    implementation("com.squareup.okhttp3:okhttp:4.9.1")

}