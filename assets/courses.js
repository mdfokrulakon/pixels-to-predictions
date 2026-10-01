/* HOW TO ADD A COURSE: 1) put its page in courses/  2) add one object to COURSES below  3) commit & push. */
window.TRACKS = [
  {id:"image-processing", name:"Image Processing", icon:"🖼️", color:"#ec4899", blurb:"Filters, transforms, segmentation and everything that happens to a pixel."},
  {id:"data-analysis", name:"Data Analysis", icon:"📊", color:"#6366f1", blurb:"Clean, explore, visualise and forecast real-world data."},
  {id:"machine-learning", name:"Machine Learning", icon:"🤖", color:"#10b981", blurb:"Models that learn from data: from regression to ensembles."},
  {id:"deep-learning", name:"Deep Learning", icon:"🧠", color:"#f59e0b", blurb:"Neural networks, training tricks and modern architectures."},
  {id:"computer-vision", name:"Computer Vision", icon:"👁️", color:"#06b6d4", blurb:"Teach machines to see: detection, recognition and more."}
];
window.COURSES = [
  {title:"Time Series Analysis and Forecasting", track:"data-analysis", level:"Beginner to Intermediate", time:"About 12 weeks", modules:"16 modules + 4 appendices", url:"courses/time-series.html",
   blurb:"From pandas datetime basics to ARIMA, SARIMAX and machine-learning forecasts, with practice tasks, quizzes and an answer key."}
];
