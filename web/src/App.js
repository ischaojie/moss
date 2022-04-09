import React, { useState, useEffect } from 'react';
import logo from './logo.svg';
import './App.css';
import './cal-heatmap.css';
import { Button, Page, Text } from '@geist-ui/core'
import CalHeatMap from 'cal-heatmap';


export default function App() {

  return (
    <div className="App flex justify-center">
      <Page>
        <Text h1>我的目标</Text>
        <Heatmap name="Github" data="http://127.0.0.1:8000/db.json"/>
        <Heatmap name="Duolingo" data="http://127.0.0.1:8000/db.json"/>
        <Heatmap name="Keep" data="http://127.0.0.1:8001/db.json"/>
      </Page>

    </div>
  );
}

function Heatmap(props) {
const cal = new CalHeatMap();
const cal_id = "cal-heatmap-" + Math.floor(Math.random() * 1000);

  useEffect(() => {
    cal.init({
      itemSelector: "#" + cal_id,
      domain: "year",
      subDomain: "day",
      data: props.data,
      start: new Date(),
      cellSize: 12,
      cellPadding: 3,
      cellRadius: 2,
      range: 1,
      legend: [20, 40, 60, 80]
    });
  });
  return (
    <div className="my-12">
      <Text h3>{props.name}</Text>
      <div className="my-2" id={cal_id}></div>
    </div>
  );
}