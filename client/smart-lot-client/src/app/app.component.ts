import { Component } from '@angular/core';
import {
  transition,
  trigger,
  query,
  style,
  animate,
  group,
  animateChild
} from '@angular/animations';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  animations: [
    trigger('fadeAnimation', [

      transition( '* => *', [

          query(':enter', 
              [
                  style({ opacity: 0 })
              ], 
              { optional: true }
          ),

          query(':leave', 
              [
                  style({ opacity: 1 }),
                  animate('0.2s', style({ opacity: 0 }))
              ], 
              { optional: true }
          ),

          query(':enter', 
              [
                  style({ opacity: 0 }),
                  animate('0.2s', style({ opacity: 1 }))
              ], 
              { optional: true }
          )

      ])

  ])]
})
export class AppComponent {
  title = 'SMART LOT';
  aboutPageActive: boolean = false
  nightMode: boolean = false

  onAboutPage() {
    this.aboutPageActive = !this.aboutPageActive
  }

  changeVisibility() {
    this.nightMode = !this.nightMode;
    if (this.nightMode === true) {
      document.body.style.backgroundColor = "#2d2d2d"
      document.body.style.color = "#edf3ff"

    }
    else {
      document.body.style.backgroundColor = "white"
      document.body.style.color = "black"

    }
    

  }


}


