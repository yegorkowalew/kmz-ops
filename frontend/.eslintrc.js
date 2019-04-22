module.exports = {
  root: true,
  env: {
    browser: true,
    node: true
  },
  parserOptions: {
    parser: 'babel-eslint'
  },
  extends: [
    '@nuxtjs',
    'plugin:nuxt/recommended'
    // 'plugin:vue/recommended'
  ],
  // add your custom rules here
  rules: {
  "vue/html-self-closing": ["error", {
    "html": {
      "void": "any",
      "normal": "any",
      "component": "any"
    },
    "svg": "any",
    "math": "any"
  }]
}
}
