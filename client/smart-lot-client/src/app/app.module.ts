import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './components/app.component';
import { MatExpansionModule, MatCardModule, MatButtonModule, MatListModule, MatProgressSpinnerModule, MatDividerModule, MatTooltipModule, MatDialogModule, MatSlideToggleModule } from '@angular/material';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HomeComponent } from './components/home/home.component';
import { AboutComponent } from './components/about/about.component';
import { CookieService } from 'ngx-cookie-service';
import { LotModalComponent } from './components/lot/lot-modal/lot-modal.component';
import { LotComponent } from './components/lot/lot.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    AboutComponent,
    LotModalComponent,
    LotComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatExpansionModule,
    MatCardModule,
    MatButtonModule,
    MatListModule,
    MatProgressSpinnerModule,
    HttpClientModule,
    MatDividerModule,
    MatTooltipModule,
    MatDialogModule,
    MatSlideToggleModule
  ],
  providers: [CookieService],
  bootstrap: [AppComponent],
  entryComponents: [LotModalComponent]
})
export class AppModule { }
