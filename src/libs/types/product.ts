import { ObjectId } from "mongoose";

import {
  ProductStatus,
  ProductSize,
  ProductCollection,
} from "../enums/product.enum";

export interface Product {
  _id: ObjectId;
  productStatus: ProductStatus;
  productCollection: ProductCollection;
  productName: string;
  productPrize: number;
  productLeftCount: number;
  productSize?: ProductSize;
  productVolume?: number;
  productDesc?: string;
  productImages: string[];
  productView: number;
}

export interface ProductInput {
  productStatus?: ProductStatus;
  productCollection: ProductCollection;
  productName: string;
  productPrize: number;
  productLeftCount: number;
  productSize?: ProductSize;
  productVolume?: number;
  productDesc?: string;
  productImages?: string[];
  productView?: number;
}
