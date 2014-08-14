from openerp.osv import osv, fields
from datetime import datetime
class product_product(osv.osv):
    def _get_product_incr(self,cr,uid,context=None):
        sql="Select prod_incr from product_product order by prod_incr desc limit 1"
        rec = []
        cr.execute(sql)
        rec = cr.dictfetchall()
        print rec
        start=1000
        id_max=1
        if(len(rec)>0):
            if(rec[0]['prod_incr']!=None):
                id_max= rec[0]['prod_incr']+1
        else:
            id_max= 1+ start
        print id_max
        return id_max
    def _generate_default_code(self,cr,uid,category_code,context=None):
        pre_str=category_code
        suff_str=''
        
        char_max=4
        id_max=self._get_product_incr(cr, uid, context)
        print id_max
        if(len(str(id_max))<char_max):
            leng_suff_str= char_max- len(str(id_max))
            for i in xrange(0,leng_suff_str):
                suff_str=suff_str+'0'
            suff_str= suff_str+str(id_max)
        else:
            suff_str= str(id_max)
        str_code= pre_str+ suff_str
        return str_code
    _inherit='product.product'
    _columns={
              'product_ids': fields.many2many('product.product', 'product_product_rel', 'product_contain_id', 'product_id', 'Product Element',),
              'parent_id': fields.many2one('product.product', 'Parent Product'),
              'child_ids': fields.one2many('product.product', 'parent_id', 'Children Product'),
              'product_size':fields.text('Product Size'),
              'product_packaging':fields.text('Product Packaging',size=256),
              'product_pack_cont_id':fields.one2many('product.pack.cont','product_id','Number Pack In Container'),
              'product_supplier_id':fields.many2one('product.supplier','Product Supplier'),
              'pack_carton_size':fields.text('Packing Carton Size'),
              'prod_incr':fields.integer('Product Increment'),
              'prod_moq':fields.integer('Product MOQ'),
              'product_list_price_his':fields.one2many('product.list.price.his','product_id','Price History'),
              'product_cost_his':fields.one2many('product.cost.his','product_id','Cost History'),
              }
    _defaults={
              # 'default_code':_generate_default_code,
               'prod_incr':_get_product_incr,
               'prod_moq':100
               }
    def onchange_categ_id(self,cr,uid,ids,categ_id,context=None):
        category_code = self.pool.get('product.category').browse(cr,uid,[categ_id])[0].code
        if(category_code==False):
            category_code='HG'
        default_code= self._generate_default_code(cr, uid, category_code, context)
        print default_code
        return {'value': {'default_code': default_code}}
    def onchange_sale_price(self, cr, uid, ids, sale_price, context=None):
        print ids
        if len(ids)==0:
            return True
        values={}
        values.update({'list_price':sale_price,'user_id':uid,'date_modified':datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'product_id':ids[0]})
        print values
        prod_price_his_obj = self.pool.get('product.list.price.his')
        prod_price_his_obj.create(cr,uid,values,context)
        return True
    def onchange_cost(self, cr, uid, ids, standard_price, context=None):
        print ids
        if len(ids)==0:
            return True
        values={}
        values.update({'cost':standard_price,'user_id':uid,'date_modified':datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'product_id':ids[0]})
        print values
        prod_price_his_obj = self.pool.get('product.cost.his')
        prod_price_his_obj.create(cr,uid,values,context)
        return True
    
class product_pack_cont(osv.osv):
    _name='product.pack.cont'
    _columns={
              'product_id':fields.many2one('product.product','Product ID'),
              'number_pack':fields.integer('Number Pack'),
              'cont_type':fields.char('Container Type'),
              }

class product_category(osv.osv):
    _inherit='product.category'
    _columns={
              'code':fields.char('Category Code',size=12),
              }
class product_list_price_history(osv.osv):
    _name='product.list.price.his'
    _columns={
              'product_id':fields.many2one('product.product','Product ID'),
              'list_price':fields.float('Price'),
              'date_modified':fields.datetime('Date Modified'),
              'user_id': fields.many2one('res.users', 'Person'),
              'note':fields.text('Note')
               
               }
class product_cost_history(osv.osv):
    _name='product.cost.his'
    _columns={
              'product_id':fields.many2one('product.product','Product ID'),
              'cost':fields.float('Cost'),
              'date_modified':fields.datetime('Date Modified'),
              'user_id': fields.many2one('res.users', 'Person'),
              'note':fields.text('Note')
               
               }