import { Component, OnInit } from '@angular/core';
import {Location} from '@angular/common';
import { CookieService } from 'ngx-cookie-service';
import { MatSlideToggleChange } from '@angular/material';
import { FormControl } from '@angular/forms';

@Component({
  selector: 'app-about',
  templateUrl: './about.component.html',
  styleUrls: ['./about.component.scss']
})
export class AboutComponent implements OnInit {

  colorblindMode:boolean
  nightMode:boolean

  constructor(private location: Location, private cookie:CookieService) { }  

  backClicked() {
    this.location.back()
  }
  ngDoCheck() {
    if (this.cookie.get('colorblindModeCookie') === 'true') {
      this.colorblindMode = true
    }
    else{
      this.colorblindMode = false
    }

    if (this.cookie.get('nightModeCookie') === 'true'){
      this.nightMode = true
    }
    else{
      this.nightMode = false
    }
  }
  
  ColorblindModeToggle = new FormControl()
  onChangeColorblindMode(ob: MatSlideToggleChange) {
    if (ob.checked === true) {
      this.cookie.set('colorblindModeCookie','true')
    }
    else if (ob.checked === false) {
      this.cookie.set('colorblindModeCookie','false')
    }
  }

  NightModeToggle = new FormControl()
  onChangeNightMode(ob: MatSlideToggleChange) {
    if (ob.checked === true) {
      this.cookie.set('nightModeCookie','true')
    }
    else if (ob.checked === false) {
      this.cookie.set('nightModeCookie','false')
    }
  }

  ngOnInit() {}
}
