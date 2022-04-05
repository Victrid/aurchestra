const path = require('path');
const webpack = require('webpack')
const { VueLoaderPlugin } = require('vue-loader')

function root(__path) {
  return path.join(__dirname, __path);
}

module.exports = {
  // this is the entry file for webpack
  entry: './src/main.js', 
  //mode
  mode: "development",
  // compiled/built output file
  output: {
    path: path.resolve(__dirname, 'public/javascripts'),
    filename: 'index.js',
    // this must be same as Express static use. 
    // Check ./app.js
    publicPath: '/javascripts/',
  },
  module:{
    rules:[
        {
            test: /\.vue$/,
            loader: 'vue-loader'
        },
        {
          test: /\.pug$/,
          loader: 'pug-plain-loader'
        },
        {
          test: /\.css$/i,
          use: ["style-loader", "css-loader"],
        },
    ],
  },
  devServer: {
    static: "./",
    port: 8080,
    proxy:{
        "/":{
            target: 'http://localhost:3000' ,
            secure: false,
        },
    },
  },
  resolve: {
    alias: { 
      // we have to use Vue Es Modules compatible build
      'vue$': 'vue/dist/vue.esm-bundler.js',
    },
    fallback: {
      "fs": false,
      "tls": false,
      "net": false,
      "path": false,
      "zlib": false,
      "http": false,
      "https": false,
      "stream": false,
      "crypto": false,
      "util": require.resolve("util/"),
      "url": require.resolve("url/"),
      "assert": require.resolve("assert/"),
      "buffer": require.resolve("buffer/"),
      "os": false,
      // "crypto-browserify": require.resolve('crypto-browserify'), //if you want to use this module also don't forget npm i crypto-browserify 
    } 
  },
  plugins:[
    new webpack.DefinePlugin({
        __VUE_OPTIONS_API__: JSON.stringify(true),
        __VUE_PROD_DEVTOOLS__: JSON.stringify(true),
      }),
    new VueLoaderPlugin(),
    new webpack.ContextReplacementPlugin( 
      /Sequelize(\\|\/)/, 
      path.resolve(__dirname, '../src') ),
  ],

  externals: ['express']
};
