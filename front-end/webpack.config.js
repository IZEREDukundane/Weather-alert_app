#Basic webpack setup for React

const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const Dotenv = require("dotenv-webpack");

module.exports = {
  mode: process.env.NODE_ENV || "development", // "development" or "production"
  entry: "./src/index.js", // Entry point of the app
  output: {
    path: path.resolve(__dirname, "dist"), // Output folder
    filename: "bundle.js",
    clean: true, // Clean output folder before building
  },
  module: {
    rules: [
      {
        test: /\.js$|\.jsx$/, // For JS and JSX files
        exclude: /node_modules/,
        use: "babel-loader",
      },
      {
        test: /\.css$/, // CSS support
        use: ["style-loader", "css-loader"],
      },
      {
        test: /\.(png|jpg|jpeg|gif|svg)$/i, // Image files
        type: "asset/resource",
      },
    ],
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: "./public/index.html", // HTML template
      filename: "index.html",
    }),
    new Dotenv(), // Loads .env variables
  ],
  devServer: {
    static: path.join(__dirname, "public"), // Serve static files
    compress: true, // Enable gzip compression
    port: 3000, // Local dev server port
    hot: true, // Hot module replacement
    historyApiFallback: true, // Supports React Router
  },
  resolve: {
    extensions: [".js", ".jsx"], // Auto-resolve these extensions
  },
};
