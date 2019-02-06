import { Component, OnInit } from '@angular/core';
import {MatExpansionModule, matExpansionAnimations, MatButtonModule, MatNavList} from '@angular/material';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  links = ["Nethken A"]

  constructor() { }

  ngOnInit() {
  }

}
