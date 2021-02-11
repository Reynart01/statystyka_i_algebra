select pp.price_date, pp.price, p.name, s.name from wegrodzki.products p
  join  wegrodzki.products_prices pp
  on pp.product_id = p.product_id
  join wegrodzki.sellers s
  on pp.seller_id = s.seller_id
  where p.name like :name and pp.price_date between TO_DATE(:startDate, 'YYYY-MM-DD') and TO_DATE(:endDate, 'YYYY-MM-DD')
  order by pp.product_price_id