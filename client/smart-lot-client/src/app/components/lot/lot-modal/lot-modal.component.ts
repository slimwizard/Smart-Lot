import { Component, OnInit } from '@angular/core';
import {MatDialogRef} from '@angular/material'

@Component({
  selector: 'app-lot-modal',
  templateUrl: './lot-modal.component.html',
  styleUrls: ['./lot-modal.component.scss']
})
export class LotModalComponent implements OnInit {

  constructor(private dialogRef: MatDialogRef<LotModalComponent>) {}

  lot_uri: string = window.location.pathname.split("/").slice(-1)[0];
  lot_image1: string = `../../../../assets/${this.lot_uri}-1.jpg`
  lot_image2: string = `../../../../assets/${this.lot_uri}-2.jpg`

  onClick(): void {
    this.dialogRef.close()
    let body = document.getElementsByTagName('html')
    body[0].blur()
    }

  ngOnInit() {
  }

}
