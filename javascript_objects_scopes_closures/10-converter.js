#!/usr/bin/node
'use strict';

exports.converter = function (base) {
  return function (n) {
    return n.toString(base);
  };
};
